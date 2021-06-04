from rest_framework.routers import DefaultRouter

from .viewsets import UserViewSet, PostViewSet, ReactionViewSet, CommentViewSet

router = DefaultRouter()

router.register("users", UserViewSet)
router.register("posts", PostViewSet)
router.register("reactions", ReactionViewSet)
router.register("comments", CommentViewSet)
