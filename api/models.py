from django.db import models
from django.conf import settings
from django.utils import timezone


class Post(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField(max_length=1000)
    published = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(null=True)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        # "auth.User",
        on_delete=models.CASCADE,
        # null=True,
        related_name="posts",
    )

    def __str__(self):
        return self.title


class Comment(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField(max_length=1000)
    published = models.DateTimeField(default=timezone.now)
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name="comments",
    )
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        # "auth.User",
        on_delete=models.CASCADE,
        # null=True,
        related_name="comments",
    )

    def __str__(self):
        return self.title


class Reaction(models.Model):
    type = models.CharField(max_length=50)
    published = models.DateTimeField(default=timezone.now)
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name="reactions",
    )
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        # "auth.User",
        on_delete=models.CASCADE,
        # null=True,
        related_name="reactions",
    )

    def __str__(self):
        return self.type
