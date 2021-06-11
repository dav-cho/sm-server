from rest_framework import serializers

from rest_framework_simplejwt.tokens import Token

from .models import User


# class UserSerializer(serializers.Serializer):
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "email",
            "username",
            "password",
            "last_login",
            "created",
            "posts",
            "comments",
            "reactions",
        ]
        extra_kwargs = {"password": {"write_only": True}}
