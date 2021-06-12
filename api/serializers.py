from django.db.models.query import QuerySet
from rest_framework import serializers

from accounts.models import User
from .models import Post, Comment, Reaction


class PostSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()
    author_id = serializers.PrimaryKeyRelatedField(read_only=True)
    # comments = serializers.StringRelatedField(many=True)
    class Meta:
        model = Post
        fields = (
            "id",
            "title",
            "author",
            "author_id",
            "published",
            "body",
            "reactions",
            "comments",
        )


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()
    author_id = serializers.StringRelatedField()

    class Meta:
        model = Comment
        fields = ("id", "post", "published", "title", "body", "author", "author_id")


class ReactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reaction
        fields = ("id", "post", "author", "published", "type")
