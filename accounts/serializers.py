from rest_framework import serializers

from .models import User
from api.serializers import PostSerializer, CommentSerializer, ReactionSerializer


class UserSerializer(serializers.ModelSerializer):
    posts = PostSerializer(many=True)
    comments = CommentSerializer(many=True)
    reactions = ReactionSerializer(many=True)

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


class CurrentUserSerializer(serializers.ModelSerializer):
    posts = PostSerializer(many=True)
    comments = CommentSerializer(many=True)
    reactions = ReactionSerializer(many=True)

    class Meta:
        model = User
        exclude = ["password", "is_admin", "is_superuser", "is_staff"]
