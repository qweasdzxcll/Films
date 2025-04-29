from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    phone = serializers.CharField()
    password = serializers.CharField()
    class Meta:
        model = User
        fields = ['phone', 'password']

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        return user

