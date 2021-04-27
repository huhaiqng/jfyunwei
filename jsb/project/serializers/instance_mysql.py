from rest_framework import serializers
from project.models import MySQLInstance


# MySQL 实例
class MySQLInstanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = MySQLInstance
        fields = '__all__'
