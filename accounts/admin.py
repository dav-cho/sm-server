from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import User


class UserAdmin(BaseUserAdmin):
    list_display = (
        "id",
        "email",
        "username",
        "last_login",
        "created",
        "is_admin",
        "is_superuser",
        "is_staff",
        "is_active",
    )
    # list_filter = ("email", "username")
    fieldsets = (
        (None, {"fields": ("email", "username", "password")}),
        ("Permissions", {"fields": ("is_admin", "is_superuser", "is_staff")}),
        ("Groups", {"fields": ("groups",)}),
    )
    search_fields = ("email", "username")
    ordering = ("email",)
    filter_horizontal = ()


admin.site.register(User, UserAdmin)
