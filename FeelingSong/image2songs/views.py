from django.shortcuts import render
from django.http import HttpResponse
from image2songs.models import UserData, Feeling
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from .spotifyCreateList import createlist


# Create your views here.

class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'image2songs/register.html'


def index(request):
    return render(request, 'image2songs/index.html')


def base(request):
    return render(request, 'image2songs/base.html')


def register(request):
    return render(request, 'image2songs/register.html')


def webcam(request):
    return render(request, 'image2songs/webcam.html')


def historial(request):
    return render(request, 'image2songs/historial.html')


def upload(request):
    if request.GET.get('url'):
        createlist(request.GET.get('imageurl'))
    return render(request, 'image2songs/upload.html')
