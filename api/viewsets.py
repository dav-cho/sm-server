from django.db.models import F
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny, IsAuthenticated

from .models import Post, Reaction, Comment
from .serializers import (
    PostSerializer,
    CommentSerializer,
    ReactionSerializer,
)
from .permissions import IsAuthorOrReadOnly


class PostViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]
    queryset = Post.objects.all().order_by(
        F("updated").desc(nulls_last=True), "-published"
    )
    serializer_class = PostSerializer


class CommentViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class ReactionViewSet(ModelViewSet):
    permission_classes = [AllowAny]
    queryset = Reaction.objects.all()
    serializer_class = ReactionSerializer
