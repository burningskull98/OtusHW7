"""
Этот модуль отвечает за определение моделей данных в приложении.
"""
from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey("User", on_delete=models.CASCADE, related_name="posts")
    tags = models.ManyToManyField("Tag", related_name="posts")

    def __str__(self):
        return self.title


class Comment(models.Model):
    text = models.TextField()
    user = models.ForeignKey("User", on_delete=models.CASCADE, related_name="comments")
    pub_date = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")

    def __str__(self):
        return f"Comment by {self.user} on {self.post}"


class User(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    bio = models.TextField()
    website = models.URLField(blank=True, null=True)

    def __str__(self):
        return f"Profile for {self.user}"


class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
