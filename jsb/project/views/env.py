from rest_framework import viewsets
from project.models import Env
from project.serializers import EnvSerializer


# 环境
class EnvViewSet(viewsets.ModelViewSet):
    queryset = Env.objects.all().order_by('name')
    serializer_class = EnvSerializer
    pagination_class = None
