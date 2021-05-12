from rest_framework import serializers
from .url import UrlSerializer
from .host import ProjectHostSerializer
from project.models import Project, Host


class ProjectSerializer(serializers.ModelSerializer):
    urls = UrlSerializer(read_only=True, many=True)
    hosts = ProjectHostSerializer(read_only=True, many=True)

    class Meta:
        model = Project
        fields = '__all__'


class ProjectForConfigSerializer(serializers.ModelSerializer):

    class Meta:
        model = Project
        fields = ['id', 'name']


class GetHostSerializer(serializers.ModelSerializer):
    project = ProjectForConfigSerializer(read_only=True, many=True)

    class Meta:
        model = Host
        fields = '__all__'
