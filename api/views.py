from rest_framework.permissions import DjangoModelPermissions
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from .models import Post, Comment, Reaction
from .serializers import PostSerializer, CommentSerializer, ReactionSerializer
from .permissions import (
    PostUserPermission,
    CommentUserPermission,
    ReactionUserPermission,
)


class PostList(ListCreateAPIView):
    permission_classes = [DjangoModelPermissions]
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetail(RetrieveUpdateDestroyAPIView, PostUserPermission):
    permission_classes = [PostUserPermission]
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class CommentList(ListCreateAPIView):
    permission_classes = [DjangoModelPermissions]
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class ReactionList(ListCreateAPIView):
    permission_classes = [DjangoModelPermissions]
    queryset = Reaction.objects.all()
    serializer_class = ReactionSerializer
