from rest_framework import serializers
from address.models import Host


class HostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Host
        fields = '__all__'


class ProjectHostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Host
        fields = ['name', 'hostname', 'inside_ip', 'env']
