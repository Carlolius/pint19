from django.shortcuts import render
from django.http import HttpResponse
from image2songs.models import UserData, Feeling
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from .spotifyCreateList import createlist
from .authenticateSpotify import *

from django.views.decorators.csrf import csrf_exempt, csrf_protect

# Create your views here.

class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'image2songs/register.html'

@csrf_protect
def index(request):
    sp_oauth = gettoken(request)
    token = sp_oauth.get_cached_token()
    if token:
        return render(request, 'image2songs/index.html')
    else:
        authenticate(request)
        return render(request, 'image2songs/index.html')

@csrf_protect
def base(request):
    return render(request, 'image2songs/base.html')

@csrf_protect
def register(request):
    return render(request, 'image2songs/register.html')

@csrf_protect
def webcam(request):
    return render(request, 'image2songs/webcam.html')

@csrf_protect
def historial(request):
    return render(request, 'image2songs/historial.html')

@csrf_protect
def upload(request):
    if request.GET.get('url'):
        createlist(request, request.GET.get('imageurl'))
    if request.GET.get('file'):
        createlist(request, request.GET.get('imagefile'))
    return render(request, 'image2songs/upload.html')

@csrf_exempt
def process(request):
    if request.is_ajax():
        request_data = request.POST
        imageUrl = request_data['imageUrl']
        createlist(request, imageUrl)
    return render(request, 'image2songs/upload.html')

@csrf_exempt
def callback(request):
    token = ((str(request).split(" "))[2])[:-2]
    savetoken(request, token)
    return render(request, 'image2songs/callback.html')
