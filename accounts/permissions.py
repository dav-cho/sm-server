from rest_framework.permissions import BasePermission, SAFE_METHODS


class UserPermission(BasePermission):
    message = "Only the owner can view this account."

    def has_object_permission(self, req, view, obj):
        if req.method in SAFE_METHODS:
            return True
        return obj.author == req.user


class UserProfilePermission(BasePermission):
    message = "Only the owner can view this profile."

    def has_object_permission(self, req, view, obj):
        if req.method in SAFE_METHODS:
            return True
        return obj.author == req.user
