from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from project.serializers import ProjectSerializer, ProjectForConfigSerializer
from project.models import Project


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [AllowAny]


class ProjectForConfigViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectForConfigSerializer
    permission_classes = [AllowAny]
