from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    category = models.CharField(max_length=60)
    class Meta:
        ordering = ('category',)
    def __str__(self):
        return self.category

class Posts(models.Model):
    title = models.CharField(max_length=60)
    category = models.ForeignKey(Category)
    post = models.TextField(max_length=10000)
    creator = models.ForeignKey(User)
    created = models.DateTimeField(auto_now_add=True)
    edited = models.DateTimeField(auto_now=True)
    class Meta:
        ordering = ('-created',)
    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Posts, related_name='comments')
    comment = models.TextField(max_length=1000)
    creator = models.ForeignKey(User)
    created = models.DateTimeField(auto_now_add=True)
    edited = models.DateTimeField(auto_now=True)
    class Meta:
        ordering = ('-created',)
    def __str__(self):
        return self.comment
