from django.db.models import F
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAuthenticatedOrReadOnly,
)
from rest_framework_simplejwt.authentication import JWTAuthentication

from .models import Post, Reaction, Comment
from .serializers import (
    PostSerializer,
    CommentSerializer,
    ReactionSerializer,
)
from .permissions import (
    IsAuthorOrReadOnly,
    PostPermission,
    CommentUserPermission,
    ReactionUserPermission,
)

from rest_framework.generics import GenericAPIView


class PostViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]
    queryset = Post.objects.all().order_by(
        F("updated").desc(nulls_last=True), "-published"
    )
    serializer_class = PostSerializer
    # permission_classes = [IsAuthenticatedOrReadOnly]
    # permission_classes = [AllowAny]
    # authentication_classes = [JWTAuthentication]


class CommentViewSet(ModelViewSet):
    permission_classes = [AllowAny]
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class ReactionViewSet(ModelViewSet):
    permission_classes = [AllowAny]
    queryset = Reaction.objects.all()
    serializer_class = ReactionSerializer
