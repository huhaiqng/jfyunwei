from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework import viewsets
from .serializers import DailySerializer, GetDailySerializer
from .models import Daily
from auth_permission.perm import get_user_by_token


# 个人日报
class DailyViewSet(viewsets.ModelViewSet):
    queryset = Daily.objects.all()
    serializer_class = DailySerializer
    pagination_class = PageNumberPagination

    def list(self, request, *args, **kwargs):
        page_size = request.GET.get('limit')

        if int(page_size) == 10000:
            PageNumberPagination.page_size = None
        else:
            PageNumberPagination.page_size = page_size

        task = request.GET.get('task')
        user = get_user_by_token(request)
        queryset = Daily.objects.filter(task__contains=task, owner=user).order_by('-created_at')

        page = self.paginate_queryset(queryset)
        # 将 PageNumberPagination.page_size 设置为 None 以免影响其它查询
        PageNumberPagination.page_size = None
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


# 查看全部日报
class GetDailyViewSet(viewsets.ModelViewSet):
    queryset = Daily.objects.all()
    serializer_class = GetDailySerializer
    pagination_class = PageNumberPagination

    def list(self, request, *args, **kwargs):
        page_size = request.GET.get('limit')

        if int(page_size) == 10000:
            PageNumberPagination.page_size = None
        else:
            PageNumberPagination.page_size = page_size

        group = request.GET.get('group')
        user = request.GET.get('user')
        start_date = request.GET.get('start_date')
        end_date = request.GET.get('end_date')
        queryset = Daily.objects.filter(owner__username__contains=user, owner__groups__name__contains=group)\
            .exclude(owner__groups__name__in=['其它组', '管理组'])\
            .filter(created_at__range=(start_date, end_date)).order_by('owner')

        page = self.paginate_queryset(queryset)
        # 将 PageNumberPagination.page_size 设置为 None 以免影响其它查询
        PageNumberPagination.page_size = None
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
