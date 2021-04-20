from rest_framework import serializers
from .models import Host, MySQLInstance
from address.models import Env
from django_celery_results.models import TaskResult


class EnvSerializer(serializers.ModelSerializer):
    class Meta:
        model = Env
        fields = '__all__'


class HostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Host
        fields = '__all__'


class TaskResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskResult
        fields = '__all__'


# MySQL 实例
class MySQLInstanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = MySQLInstance
        fields = '__all__'

