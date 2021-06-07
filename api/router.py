from rest_framework.routers import DefaultRouter

from .viewsets import (
    UserTestViewSet,
    PostViewSet,
    ReactionViewSet,
    CommentViewSet,
)

router = DefaultRouter()

router.register("testusers", UserTestViewSet)
router.register("posts", PostViewSet)
router.register("reactions", ReactionViewSet)
router.register("comments", CommentViewSet)
