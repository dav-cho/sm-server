from django.contrib import admin

from .models import Post, Comment, Reaction


class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "body")
    list_filter = ("author", "reactions", "comments")


class CommentAdmin(admin.ModelAdmin):
    list_display = ("post", "author", "title", "body")
    filter_display = ("author", "posts")


class ReactionAdmin(admin.ModelAdmin):
    list_display = ("type", "author")
    list_filter = ("author", "post")


admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Reaction, ReactionAdmin)
