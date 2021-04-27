from rest_framework import serializers
from address.models import Env


class EnvSerializer(serializers.ModelSerializer):
    class Meta:
        model = Env
        fields = '__all__'
