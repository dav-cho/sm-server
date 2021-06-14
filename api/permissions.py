from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsAuthorOrReadOnly(BasePermission):
    message = "Only the author can edit this."

    def has_object_permission(self, req, view, obj):
        if req.method in SAFE_METHODS:
            return True
        return obj.author == req.user


class PostPermission(BasePermission):
    message = "Only the author can edit this post."

    def has_object_permission(self, req, view, obj):
        if req.method in SAFE_METHODS:
            return True
        return obj.author == req.user


class CommentUserPermission(BasePermission):
    message = "Only the author can edit this comment."

    def has_object_permission(self, req, view, obj):
        if req.method in SAFE_METHODS:
            return True
        return obj.author == req.user


class ReactionUserPermission(BasePermission):
    message = "Only the author can edit this reaction."

    def has_object_permission(self, req, view, obj):
        if req.method in SAFE_METHODS:
            return True
        return obj.author == req.user
