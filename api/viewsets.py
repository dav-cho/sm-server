from rest_framework.viewsets import ModelViewSet

from .models import UserTest, Post, Reaction, Comment

from .serializers import (
    UserTestSerializer,
    PostSerializer,
    ReactionSerializer,
    CommentSerializer,
)


class UserTestViewSet(ModelViewSet):
    queryset = UserTest.objects.all()
    serializer_class = UserTestSerializer


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class ReactionViewSet(ModelViewSet):
    queryset = Reaction.objects.all()
    serializer_class = ReactionSerializer


class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
