from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .models import Posts, Category, Comment
from django.urls import reverse

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
    if request.method == 'POST':
        categorys = request.POST['sel_cat']
        return HttpResponseRedirect(reverse('category', kwargs={'categoryss': categorys}))

    return render(request, 'discuss/category.html', {'categorys' : categorys, 'category' : category})

@login_required
def defa(request):
    category = Category.objects.all()[0]
    return HttpResponseRedirect(reverse('category', kwargs={'categoryss': category}))
