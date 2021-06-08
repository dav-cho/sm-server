from rest_framework.routers import DefaultRouter

from .viewsets import (
    PostViewSet,
    CommentViewSet,
    ReactionViewSet,
)

router = DefaultRouter()

router.register("posts", PostViewSet)
router.register("comments", CommentViewSet)
router.register("reactions", ReactionViewSet)
