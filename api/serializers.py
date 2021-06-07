from rest_framework import serializers

from .models import UserTest, Post, Reaction, Comment


class UserTestSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserTest
        fields = ("email", "username", "password")


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
