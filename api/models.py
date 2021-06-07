from django.db import models


class UserTest(models.Model):
    email = models.EmailField(max_length=100)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.username


class Post(models.Model):
    author = models.ForeignKey(
        UserTest, on_delete=models.CASCADE, null=True, related_name="posts"
    )
    title = models.CharField(max_length=200)
    body = models.TextField(max_length=1000)

    def __str__(self):
        return self.title


class Reaction(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="reactions")
    author = models.ForeignKey(
        UserTest, on_delete=models.CASCADE, null=True, related_name="reactions"
    )
    type = models.CharField(max_length=50)


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(
        UserTest, on_delete=models.CASCADE, null=True, related_name="comments"
    )
    title = models.CharField(max_length=200)
    body = models.TextField(max_length=1000)
