from django.shortcuts import render
from django.http import HttpResponse
from image2songs.models import UserData, Feeling

# Create your views here.


def index(request):
    return render(request, 'image2songs/index.html')


def base(request):
    return render(request, 'image2songs/base.html')


def register(request):
    return render(request, 'image2songs/register.html')
