from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from project.serializers import PopularUrlSerializer
from project.models import Url


class PopularUrlViewSet(viewsets.ModelViewSet):
    queryset = Url.objects.filter(popular=True).order_by('project__name', 'env__name')
    serializer_class = PopularUrlSerializer
    permission_classes = [AllowAny]
