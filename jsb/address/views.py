from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from address.serializers import AddressSerializer
from address.models import Address


class AddressViewSet(viewsets.ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    permission_classes = [AllowAny]
