from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Posts, Category, Comment

# Create your views here.

@login_required
def home(request):
    posts = Posts.objects;
    category = Category.objects.all();
    comment = Comment.objects.all();
    return render(request, 'discuss/home.html', {'posts': posts, 'category' : category, 'comment':comment, 'section': 'home'})

@login_required
def post(request, categoryss, postss):
    return render(request, 'discuss/post.html')

@login_required
def category(request, categoryss):
    return render(request, 'discuss/category.html')
