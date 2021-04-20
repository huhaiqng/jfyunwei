from rest_framework import serializers
from address.models import Address, Env, ProjectUrl, Project
from project.models import Host


class ProjectHostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Host
        fields = ['name', 'hostname', 'inside_ip', 'env']


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
    hosts = ProjectHostSerializer(read_only=True, many=True)

    class Meta:
        model = Project
        fields = '__all__'
