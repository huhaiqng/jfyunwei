from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from address.serializers import AddressSerializer
from address.models import Address
from django_filters.rest_framework import DjangoFilterBackend


class AddressViewSet(viewsets.ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    filter_backends = [DjangoFilterBackend]
    permission_classes = [AllowAny]
