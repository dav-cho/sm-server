from django.db.models import query
from rest_framework import viewsets
from rest_framework.serializers import ModelSerializer

from .models import User, Post, Reaction, Comment
from .serializers import (
    UserSerializer,
    PostSerializer,
    ReactionSerializer,
    CommentSerializer,
)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class ReactionViewSet(viewsets.ModelViewSet):
    queryset = Reaction.objects.all()
    serializer_class = ReactionSerializer


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = ModelSerializer
