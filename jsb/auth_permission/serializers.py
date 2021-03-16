from rest_framework import serializers
from .models import UserInfo, L1Menu, L2Menu
from django.contrib.auth.models import Group


# 获取单个用户信息
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserInfo
        fields = '__all__'


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'


class GetGroupSerializer(serializers.ModelSerializer):
    user_set = UserSerializer(many=True)

    class Meta:
        model = Group
        fields = '__all__'


# 二级菜单
class L2MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = L2Menu
        fields = '__all__'


# 一级菜单
class L1MenuSerializer(serializers.ModelSerializer):
    children = L2MenuSerializer(read_only=True, many=True)

    class Meta:
        model = L1Menu
        fields = '__all__'


# 增删改用户
class UserInfoInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserInfo
        fields = ['id', 'username', 'email', 'phone',  'password', 'is_superuser', 'groups', 'user_permissions']
        # fields = '__all__'


# 查询用户
class GetUserInfoSerializer(serializers.ModelSerializer):
    groups = GroupSerializer(many=True)

    class Meta:
        model = UserInfo
        fields = '__all__'

