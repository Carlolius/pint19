
from django.conf.urls import include, url
from image2songs import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    # url(r'^(?P<userData_id>\d+)/$',views.detail,name='detail'),
    url('base', views.base, name='base'),
    url('register', views.SignUp.as_view(), name='register'),
    url('webcam', views.webcam, name='webcam'),
    url(r'^login/$', auth_views.LoginView.as_view(template_name="image2songs/login.html"), name='login'),
    url(r'^logout/$', auth_views.LogoutView.as_view(template_name="image2songs/base.html"), name='logout'),
    url('upload', views.upload, name='upload'),
]
