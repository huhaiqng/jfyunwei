from rest_framework import serializers
from address.models import Address, Env, ProjectUrl, Project
from project.serializers import HostSerializer


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'


class EnvSerializer(serializers.ModelSerializer):
    class Meta:
        model = Env
        fields = '__all__'


class ProjectUrlSerializer(serializers.ModelSerializer):
    env = EnvSerializer(read_only=True)

    class Meta:
        model = ProjectUrl
        fields = '__all__'


class ProjectSerializer(serializers.ModelSerializer):
    urls = ProjectUrlSerializer(read_only=True, many=True)
    hosts = HostSerializer(read_only=True, many=True)

    class Meta:
        model = Project
        fields = '__all__'
