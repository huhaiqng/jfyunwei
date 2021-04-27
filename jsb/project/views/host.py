from rest_framework import viewsets
from rest_framework.response import Response
from project.serializers import HostSerializer
from rest_framework.pagination import PageNumberPagination
from project.models import Host


# 主机
class HostViewSet(viewsets.ModelViewSet):
    queryset = Host.objects.all()
    serializer_class = HostSerializer
    pagination_class = PageNumberPagination

    def list(self, request, *args, **kwargs):
        page_size = request.GET.get('limit')
        if int(page_size) == 10000:
            PageNumberPagination.page_size = None
        else:
            PageNumberPagination.page_size = page_size
        inside_ip = request.GET.get('inside_ip')
        env = request.GET.get('env')
        queryset = Host.objects.filter(inside_ip__contains=inside_ip, env__contains=env).order_by('inside_ip')
        page = self.paginate_queryset(queryset)

        PageNumberPagination.page_size = None
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
