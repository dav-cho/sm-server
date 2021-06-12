from rest_framework import serializers

from rest_framework_simplejwt.tokens import Token

from .models import User
from api.serializers import PostSerializer, CommentSerializer


# class UserSerializer(serializers.Serializer):
class UserSerializer(serializers.ModelSerializer):
    # posts = serializers.StringRelatedField(many=True)
    posts = PostSerializer(many=True)
    comments = CommentSerializer(many=True)

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
