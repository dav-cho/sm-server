from rest_framework.viewsets import ModelViewSet

from .models import Post, Reaction, Comment

from .serializers import (
    PostSerializer,
    CommentSerializer,
    ReactionSerializer,
)


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class ReactionViewSet(ModelViewSet):
    queryset = Reaction.objects.all()
    serializer_class = ReactionSerializer
