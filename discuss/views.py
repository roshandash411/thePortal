from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Posts, Category, Comment

# Create your views here.

@login_required
def home(request):
    posts = Posts.objects
    category = Category.objects.all()
    comment = Comment.objects.all()
    return render(request, 'discuss/home.html', {'posts': posts, 'category' : category, 'comment':comment, 'section': 'home'})

@login_required
def post(request, categoryss, postss):
    posts = Posts.objects.filter(title=postss)[0]
    comment = Comment.objects.all()
    return render(request, 'discuss/post.html', {'posts': posts, 'comment': comment})

@login_required
def category(request, categoryss):
    categorys = Category.objects.filter(category=categoryss)[0]
    category = Category.objects.all()
    return render(request, 'discuss/category.html', {'categorys' : categorys, 'category' : category})
