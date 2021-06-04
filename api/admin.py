from django.contrib import admin

from .models import User, Post, Reaction, Comment


class UserAdmin(admin.ModelAdmin):
    list_display = ("username", "email", "password")
    list_filter = ("posts", "reactions", "comments")


class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "body")
    list_filter = ("author", "reactions", "comments")


class ReactionAdmin(admin.ModelAdmin):
    list_display = ("type", "author")
    list_filter = ("author", "post")


class CommentAdmin(admin.ModelAdmin):
    list_display = ("post", "author", "title", "body")
    filter_display = ("author", "posts")


admin.site.register(User, UserAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Reaction, ReactionAdmin)
admin.site.register(Comment, CommentAdmin)
