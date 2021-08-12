from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
from guardian.models import UserObjectPermission, GroupObjectPermission
from django.contrib.auth.models import Group, ContentType
from .models import UserInfo, L1Menu, L2Menu
from .serializers import UserSerializer, L1MenuSerializer, L2MenuSerializer, GroupSerializer, UserInfoSerializer,\
     GetUserInfoSerializer, GetGroupSerializer, GetUserHostedInfoSerializer, UserObjectPermissionSerializer, \
     GroupObjectPermissionSerializer
from django_filters.rest_framework import DjangoFilterBackend
from django.contrib.auth.hashers import make_password


# 用户信息
class UserViewSet(viewsets.ModelViewSet):
    queryset = UserInfo.objects.all()
    serializer_class = UserSerializer
    filterset_fields = ('username',)


# 一级菜单
class L1MenuViewSet(viewsets.ModelViewSet):
    queryset = L1Menu.objects.all()
    serializer_class = L1MenuSerializer
    filter_backends = [DjangoFilterBackend]
    permission_classes = [IsAuthenticated]


# 二级模型菜单
class L2MenuViewSet(viewsets.ModelViewSet):
    queryset = L2Menu.objects.all()
    serializer_class = L2MenuSerializer


# 增删改组
class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


# 查询组
class GetGroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GetGroupSerializer


# 设置组的权限
class SetGroupObjectPermsView(APIView):
    permission_classes = [IsAdminUser]

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


# 获取组拥有权限的二级菜单
class GetGroupL2menuView(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request):
        groupname = request.GET.get('groupname')
        group = Group.objects.get(name=groupname)
        # 查询组的模型 l2menu 查看权限所有记录
        queryset = GroupObjectPermission.objects.filter(group=group, permission=104).values('object_pk')
        results = []
        for obj in queryset:
            results.append(int(obj['object_pk']))
        return Response(results)


# 增删改用户
class UserInfoViewSet(viewsets.ModelViewSet):
    queryset = UserInfo.objects.all().order_by('-date_joined')
    serializer_class = UserInfoSerializer

    def create(self, request, *args, **kwargs):
        request.data['password'] = make_password(request.data['password'])
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def update(self, request, *args, **kwargs):
        request.data['password'] = make_password(request.data['password'])
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)


# 查询用户
class GetUserInfoViewSet(viewsets.ModelViewSet):
    queryset = UserInfo.objects.all().order_by('date_joined')
    serializer_class = GetUserInfoSerializer
    filterset_fields = ('groups',)


# 查询用户主持
class GetUserHostedInfoViewSet(viewsets.ModelViewSet):
    queryset = UserInfo.objects.exclude(
        username__in=['jsb', 'AnonymousUser']).order_by('hosted', 'hosted_date', 'groups', 'date_joined')
    serializer_class = GetUserHostedInfoSerializer
    filter_backends = [DjangoFilterBackend]
    permission_classes = [AllowAny]


# 用户对象权限
class UserObjectPermissionViewSet(viewsets.ModelViewSet):
    queryset = UserObjectPermission.objects.all()
    serializer_class = UserObjectPermissionSerializer
    filter_backends = [DjangoFilterBackend]
    permission_classes = [IsAuthenticated]


# 组对象权限
class GroupObjectPermissionViewSet(viewsets.ModelViewSet):
    queryset = GroupObjectPermission.objects.all()
    serializer_class = GroupObjectPermissionSerializer
    filter_backends = [DjangoFilterBackend]
    permission_classes = [IsAuthenticated]
