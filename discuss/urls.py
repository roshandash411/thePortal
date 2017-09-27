from django.conf.urls import include, url
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    url(r'^(?P<categoryss>[-\w]+)', views.category, name = 'category'),
    url(r'^(?P<categoryss>[-\w]+)/(?P<postss>[-\w]+)', views.post, name = 'post'),
    url(r'^$', views.home, name = 'home'),
]
