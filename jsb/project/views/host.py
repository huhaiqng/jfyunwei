from rest_framework.response import Response
from project.serializers import HostSerializer, GetHostSerializer
from rest_framework.pagination import PageNumberPagination
from auth_permission.perm import CheckPermViewSet
from guardian.shortcuts import get_objects_for_user
from project.models import Host


# 增删改
class HostViewSet(CheckPermViewSet):
    queryset = Host.objects.all()
    serializer_class = HostSerializer


# 查
class GetHostViewSet(CheckPermViewSet):
    queryset = Host.objects.all()
    serializer_class = GetHostSerializer
    pagination_class = PageNumberPagination

    def list(self, request, *args, **kwargs):
        page_size = request.GET.get('limit')
        inside_ip = request.GET.get('inside_ip')
        cloud_user = request.GET.get('cloud_user')
        env = request.GET.get('env')

        if int(page_size) == 10000:
            PageNumberPagination.page_size = None
        else:
            PageNumberPagination.page_size = page_size

        objects = Host.objects.filter(
            inside_ip__contains=inside_ip, cloud_user__contains=cloud_user, env__contains=env
        )
        queryset = get_objects_for_user(request.user, 'project.view_%s' % self.basename, objects)

        page = self.paginate_queryset(queryset)
        PageNumberPagination.page_size = None
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
