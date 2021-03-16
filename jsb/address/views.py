from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from address.serializers import AddressSerializer, ProjectSerializer
from address.models import Address, Project


class AddressViewSet(viewsets.ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    permission_classes = [AllowAny]


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [AllowAny]

