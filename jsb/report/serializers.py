from rest_framework import serializers
from .models import Daily
from auth_permission.models import UserInfo


class DailyUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserInfo
        fields = ['id', 'username']


class DailySerializer(serializers.ModelSerializer):

    class Meta:
        model = Daily
        fields = '__all__'


# 日报
class GetDailySerializer(serializers.ModelSerializer):
    owner = DailyUserSerializer(read_only=True)

    class Meta:
        model = Daily
        fields = '__all__'
