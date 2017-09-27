from django.conf.urls import include, url
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    url(r'^search/', views.search, name = 'search'),
    url(r'^delete_post/(?P<ids>[\d]+)/', views.delete_post, name = 'delete_post'),
    url(r'^delete_comment/(?P<ids>[\d]+)/', views.delete_comment, name = 'delete_comment'),
    url(r'^(?P<categoryss>[-\w]+)/new_post', views.new_post, name = 'new_post'),
    url(r'^(?P<categoryss>[-\w]+)/(?P<postss>[-\w]+)/new_comment', views.new_comment, name = 'new_comment'),
    url(r'^(?P<categoryss>[-\w]+)/(?P<postss>[-\w]+)', views.post, name = 'post'),
    url(r'^(?P<categoryss>[-\w]+)/', views.category, name = 'category'),
    url(r'^$', views.defa, name = 'defa'),
]
