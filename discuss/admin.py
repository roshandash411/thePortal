from django.contrib import admin
from .models import Category, Posts, Comment
# Register your models here.

admin.site.register(Category)
admin.site.register(Posts)
admin.site.register(Comment)
