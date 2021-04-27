from rest_framework import viewsets
from rest_framework.response import Response
from django_celery_results.models import TaskResult
from project.serializers import TaskResultSerializer
from rest_framework.pagination import PageNumberPagination


class TaskResultViewSet(viewsets.ModelViewSet):
    queryset = TaskResult.objects.all().order_by('-date_created')
    serializer_class = TaskResultSerializer
    pagination_class = PageNumberPagination

    def list(self, request, *args, **kwargs):
        page_size = request.GET.get('limit')
        queryset = self.filter_queryset(self.get_queryset())

        if int(page_size) == 10000:
            PageNumberPagination.page_size = None
        else:
            PageNumberPagination.page_size = page_size

        page = self.paginate_queryset(queryset)
        # 将 PageNumberPagination.page_size 设置为 None 以免影响其它查询
        PageNumberPagination.page_size = None
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
