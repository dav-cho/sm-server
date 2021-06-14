from django.conf import settings
from rest_framework import serializers
from rest_framework.serializers import (
    ModelSerializer,
    SlugRelatedField,
    PrimaryKeyRelatedField,
)

from accounts.models import User
from .models import Post, Comment, Reaction
from .mixins import UpdatePostModelMixin


class ReactionSerializer(ModelSerializer):
    class Meta:
        model = Reaction
        fields = ("id", "post", "author", "published", "type")


class CommentSerializer(ModelSerializer):
    author = SlugRelatedField(queryset=User.objects.all(), slug_field="username")
    author_id = PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Comment
        fields = (
            "post",
            "id",
            "title",
            "body",
            "published",
            "author_id",
            "author",
        )


class PostSerializer(ModelSerializer, UpdatePostModelMixin):
    author = SlugRelatedField(queryset=User.objects.all(), slug_field="username")
    comments = CommentSerializer(many=True, read_only=True)
    reactions = ReactionSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = (
            "id",
            "title",
            "body",
            "published",
            "updated",
            "author",
            "author_id",
            "comments",
            "reactions",
        )
