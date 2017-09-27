from django.conf.urls import include, url
from django.contrib.auth import views as auth_views
from . import views
from discuss import views as dis_view

urlpatterns = [
    url(r'^login/$', auth_views.LoginView.as_view(), name = 'login'),
    url(r'^logout/$', auth_views.LogoutView.as_view(), name = 'logout'),
    url(r'^logout-then-login/$', auth_views.logout_then_login, name = 'logout_then_login'),
    url(r'^$', dis_view.defa, name = 'home'),
]
