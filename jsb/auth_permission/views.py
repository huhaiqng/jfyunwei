from rest_framework import viewsets, status
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from guardian.shortcuts import get_objects_for_user, assign_perm
from guardian.models import GroupObjectPermission
from django.contrib.auth.models import Group, ContentType
from django.contrib.auth.hashers import make_password
from .models import UserInfo, L1Menu, L2Menu
from .serializers import UserSerializer, L1MenuSerializer, L2MenuSerializer, GroupSerializer, UserInfoSerializer,\
     GetUserInfoSerializer, GetGroupSerializer, GetUserHostedInfoSerializer
from .perm import CheckPermViewSet, get_user_by_token


# 用户信息
class UserViewSet(viewsets.ModelViewSet):
    queryset = UserInfo.objects.all()
    serializer_class = UserSerializer

    def get_queryset(self):
        username = self.request.GET.get('username')
        queryset = UserInfo.objects.filter(username=username)
        return queryset


# 一级菜单
class L1MenuViewSet(viewsets.ModelViewSet):
    queryset = L1Menu.objects.all()
    serializer_class = L1MenuSerializer


# 二级模型菜单
class L2MenuViewSet(CheckPermViewSet):
    queryset = L2Menu.objects.all()
    serializer_class = L2MenuSerializer

    def list(self, request, *args, **kwargs):
        username = request.GET.get('username')
        user = UserInfo.objects.get(username=username)
        mdl = self.get_serializer_class().Meta.model
        app = mdl._meta.app_label
        objects = L2Menu.objects.filter()
        queryset = get_objects_for_user(user, '%s.view_%s' %(app, self.basename), objects)

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


# 获取组拥有权限的二级菜单
class GetGroupL2menuView(APIView):
    def get(self, request):
        groupname = request.GET.get('groupname')
        group = Group.objects.get(name=groupname)
        # 查询组的模型 l2menu 查看权限所有记录
        queryset = GroupObjectPermission.objects.filter(group=group, permission=104).values('object_pk')
        results = []
        for obj in queryset:
            results.append(int(obj['object_pk']))
        return Response(results)


# 增删改组
class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


# 查询组
class GetGroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GetGroupSerializer
    pagination_class = PageNumberPagination

    def list(self, request, *args, **kwargs):
        type = request.GET.get('type')
        if type == 'report':
            queryset = Group.objects.exclude(name__in=['管理组', '其它组'])
        else:
            queryset = self.filter_queryset(self.get_queryset())

        page_size = request.GET.get('limit')
        if int(page_size) == 10000:
            PageNumberPagination.page_size = None
        else:
            PageNumberPagination.page_size = page_size
        page = self.paginate_queryset(queryset)

        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


# 设置组的权限
class SetGroupObjectPermsView(APIView):
    def post(self, request, format=None):
        model = request.data['model']
        content_type = ContentType.objects.get(model=model)
        objects = request.data['objects']
        groupname = request.data['groupname']
        group = Group.objects.get(name=groupname)
        content_type_id = content_type.id
        group_id = group.id
        for i, object in enumerate(objects):
            object_pk = int(object['id'])
            # 已存在的权限
            e_perms = GroupObjectPermission.objects.filter(content_type_id=content_type_id,
                                                           object_pk=object_pk,
                                                           group_id=group_id)
            # 删除已存在的权限
            e_perms.delete()
            perms = object['perms']
            for permission_id in perms:
                gop = GroupObjectPermission(content_type_id=content_type_id,
                                            object_pk=object_pk,
                                            group_id=group_id,
                                            permission_id=permission_id)
                gop.save()
        return Response(status=status.HTTP_201_CREATED)


# 增删改用户
class UserInfoViewSet(CheckPermViewSet):
    queryset = UserInfo.objects.all().order_by('-date_joined')
    serializer_class = UserInfoSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        request.data['password'] = make_password(request.data['password'])
        serializer.is_valid(raise_exception=True)
        user = get_user_by_token(request)
        user_groups = Group.objects.filter(user=user)
        if user.has_perm('app.add_%s' % self.basename):
            self.perform_create(serializer)
            if not user.is_superuser:
                mdl = self.get_serializer_class().Meta.model
                instance = mdl.objects.get(pk=serializer.data['id'])
                if len(user_groups) == 0:
                    assign_perm('change_%s' % self.basename, instance)
                    assign_perm('view_%s' % self.basename, instance)
                    assign_perm('delete_%s' % self.basename, instance)
                else:
                    for user_group in user_groups:
                        assign_perm('change_%s' % self.basename, user_group, instance)
                        assign_perm('view_%s' % self.basename, user_group, instance)
                        assign_perm('delete_%s' % self.basename, user_group, instance)
        else:
            return Response(data='没有新增权限，请联系管理员添加权限！', status=status.HTTP_403_FORBIDDEN)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        if request.data['password'] != instance.password:
            request.data['password'] = make_password(request.data['password'])
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        user = get_user_by_token(request)
        if user.has_perm('change_%s' % self.basename, instance):
            self.perform_update(serializer)
        else:
            return Response(data='没有编辑权限，请联系管理员添加权限！', status=status.HTTP_403_FORBIDDEN)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)


# 查询用户
class GetUserInfoViewSet(CheckPermViewSet):
    queryset = UserInfo.objects.all().order_by('date_joined')
    serializer_class = GetUserInfoSerializer
    pagination_class = PageNumberPagination

    def list(self, request, *args, **kwargs):
        page_size = request.GET.get('limit')
        group = request.GET.get('group')
        type = request.GET.get('type')

        if group == '':
            if type == 'report':
                queryset = UserInfo.objects.exclude(groups__name__in=['管理组', '其它组']).order_by('date_joined')
            else:
                queryset = self.filter_queryset(self.get_queryset())
        else:
            queryset = UserInfo.objects.filter(groups=group).order_by('date_joined')

        if int(page_size) == 10000:
            PageNumberPagination.page_size = None
        else:
            PageNumberPagination.page_size = page_size
        page = self.paginate_queryset(queryset)

        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


# 查询用户主持
class GetUserHostedInfoViewSet(viewsets.ModelViewSet):
    queryset = UserInfo.objects.exclude(username__in=['jsb']).order_by('hosted', 'hosted_date', 'groups', 'date_joined')
    serializer_class = GetUserHostedInfoSerializer
    permission_classes = [AllowAny]
