import json
from rest_framework.response import Response
from django.conf import settings
from aliyunsdkalidns.request.v20150109.DescribeDomainRecordsRequest import DescribeDomainRecordsRequest
from aliyunsdkalidns.request.v20150109.DescribeDomainsRequest import DescribeDomainsRequest
from rest_framework.views import APIView
from rest_framework import viewsets
from .serializers import TaskResultSerializer
from django_celery_results.models import TaskResult
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


class GetGaingon666Domain(APIView):
    def get(self, request, format=None):
        client = settings.ALIAPI_GAINHON666
        page = request.GET.get('page')
        per_page = request.GET.get('per_page')

        req = DescribeDomainsRequest()
        req.set_accept_format('json')

        req.set_PageNumber(page)
        req.set_PageSize(per_page)

        res = client.do_action_with_exception(req).decode('utf-8')
        return Response(json.loads(res))


class GetGaingon666DomainRecord(APIView):
    def get(self, request, format=None):
        domain_name = request.GET.get('domain_name')
        page = request.GET.get('page')
        per_page = request.GET.get('per_page')

        client = settings.ALIAPI_GAINHON666
        req = DescribeDomainRecordsRequest()
        req.set_accept_format('json')

        req.set_DomainName(domain_name)
        req.set_PageNumber(page)
        req.set_PageSize(per_page)

        res = client.do_action_with_exception(req).decode('utf-8')

        return Response(json.loads(res))


class GetLingfannaoDomain(APIView):
    def get(self, request, format=None):
        client = settings.ALIAPI_LINGFANNAO
        page = request.GET.get('page')
        per_page = request.GET.get('per_page')

        req = DescribeDomainsRequest()
        req.set_accept_format('json')

        req.set_PageNumber(page)
        req.set_PageSize(per_page)

        res = client.do_action_with_exception(req).decode('utf-8')
        return Response(json.loads(res))


class GetLingfannaoDomainRecord(APIView):
    def get(self, request, format=None):
        domain_name = request.GET.get('domain_name')
        page = request.GET.get('page')
        per_page = request.GET.get('per_page')

        client = settings.ALIAPI_LINGFANNAO
        req = DescribeDomainRecordsRequest()
        req.set_accept_format('json')

        req.set_DomainName(domain_name)
        req.set_PageNumber(page)
        req.set_PageSize(per_page)

        res = client.do_action_with_exception(req).decode('utf-8')

        return Response(json.loads(res))
