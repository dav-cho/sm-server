from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny, IsAuthenticated

from .models import Post, Reaction, Comment
from .serializers import (
    PostSerializer,
    CommentSerializer,
    ReactionSerializer,
)
from .permissions import (
    PostPermission,
    PostUserPermission,
    CommentUserPermission,
    ReactionUserPermission,
)


class PostViewSet(ModelViewSet):
    permission_classes = [PostPermission]
    # permission_classes = [AllowAny]
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class CommentViewSet(ModelViewSet):
    permission_classes = [AllowAny]
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class ReactionViewSet(ModelViewSet):
    permission_classes = [AllowAny]
    queryset = Reaction.objects.all()
    serializer_class = ReactionSerializer
