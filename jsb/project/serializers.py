from rest_framework import serializers
from .models import Host
from django_celery_results.models import TaskResult


class HostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Host
        fields = '__all__'


class TaskResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskResult
        fields = '__all__'
