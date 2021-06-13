from rest_framework.permissions import BasePermission, SAFE_METHODS

from .models import Post, Comment, Reaction
from .serializers import PostSerializer, CommentSerializer, ReactionSerializer


class IsOwnerOrReadOnly(BasePermission):
    message = "Only the owner can edit this."

    def has_object_permission(self, req, view, obj):
        if req.method in SAFE_METHODS:
            return True
        return obj.owner == req.user


class PostPermission(BasePermission):
    message = "Base Post Permission"

    def has_object_permission(self, req, view, obj):
        if req.method in SAFE_METHODS:
            return True
        return obj.author == req.user


class PostUserPermission(BasePermission):
    message = "Only the owner can edit this post."

    def has_object_permission(self, req, view, obj):
        if req.method in SAFE_METHODS:
            return True
        return obj.author == req.user


class CommentUserPermission(BasePermission):
    message = "Only the owner can edit this comment."

    def has_object_permission(self, req, view, obj):
        if req.method in SAFE_METHODS:
            return True
        return obj.author == req.user


class ReactionUserPermission(BasePermission):
    message = "Only the owner can edit this reaction."

    def has_object_permission(self, req, view, obj):
        if req.method in SAFE_METHODS:
            return True
        return obj.author == req.user
