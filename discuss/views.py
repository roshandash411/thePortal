from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .models import Posts, Category, Comment
from .forms import PostForm, CommentForm
from django.urls import reverse

# Create your views here.

@login_required
def home(request):
    posts = Posts.objects
    category = Category.objects.all()
    comment = Comment.objects.all()
    return render(request, 'discuss/home.html', {'posts': posts, 'category' : category, 'comment':comment, 'section': 'home', 'categorys' : categoryss})

@login_required
def post(request, categoryss, postss):
    posts = Posts.objects.filter(title=postss)[0]
    comment = Comment.objects.all()
    user = request.user
    return render(request, 'discuss/post.html', {'posts': posts, 'comment': comment, 'categorys' : categoryss, 'user':user})

@login_required
def category(request, categoryss):
    categorys = Category.objects.filter(category=categoryss)[0]
    category = Category.objects.all()
    if request.method == 'POST':
        categorys = request.POST['sel_cat']
        return HttpResponseRedirect(reverse('category', kwargs={'categoryss': categorys}))
    user = request.user
    return render(request, 'discuss/category.html', {'categorys' : categorys, 'category' : category, 'user': user})

@login_required
def defa(request):
    category = Category.objects.all()[0]
    return HttpResponseRedirect(reverse('category', kwargs={'categoryss': category}))

@login_required
def new_post(request, categoryss):
    if request.method == "POST":
        post_form = PostForm(data=request.POST)
        if post_form.is_valid():
            new_postz = post_form.save(commit = False)
            new_postz.category = Category.objects.filter(category=categoryss)[0]
            new_postz.creator = request.user
            new_postz.save()
            return HttpResponseRedirect(reverse('category', kwargs={'categoryss': categoryss}))

@login_required
def new_comment(request, categoryss, postss):
    if request.method == "POST":
        post_form = CommentForm(data=request.POST)
        if post_form.is_valid():
            new_postz = post_form.save(commit = False)
            new_postz.post = Posts.objects.filter(title=postss)[0]
            new_postz.creator = request.user
            new_postz.save()
            return HttpResponseRedirect(reverse('post', kwargs={'categoryss': categoryss, 'postss':postss}))

@login_required
def delete_post(request, ids):
    lel = Posts.objects.get(pk=ids)
    categoryss = lel.category
    lel.delete()
    return HttpResponseRedirect(reverse('category', kwargs={'categoryss': categoryss}))

@login_required
def delete_comment(request, ids):
    lel = Comment.objects.get(pk=ids)
    post = lel.post
    categoryss = post.category
    lel.delete()
    return HttpResponseRedirect(reverse('post', kwargs={'categoryss': categoryss, 'postss': post}))
