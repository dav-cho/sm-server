from rest_framework import serializers

from .models import User, Post, Reaction, Comment


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("email", "username", "password", "posts", "reactions", "comments")


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ("title", "author", "body", "reactions", "comments")


class ReactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reaction
        fields = ("post", "author", "type")


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ("post", "author", "title", "body")
