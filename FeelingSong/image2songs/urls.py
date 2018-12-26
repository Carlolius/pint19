
from django.conf.urls import include, url
from image2songs import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    # url(r'^(?P<userData_id>\d+)/$',views.detail,name='detail'),
    url('base', views.base, name='base'),
    url('register', views.register, name='register'),
    url('webcam', views.webcam, name='webcam'),
]
