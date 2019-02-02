from django.shortcuts import render
from django.http import HttpResponse
from image2songs.models import UserData, Feeling
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from .spotifyCreateList import createlist
from .authenticateSpotify import *
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.shortcuts import redirect
import os

from django.views.decorators.csrf import csrf_exempt, csrf_protect

# Create your views here.

class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'image2songs/register.html'

@csrf_protect
def index(request):
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

@csrf_exempt
def upload(request):
    sp_oauth = gettoken(request)
    token = sp_oauth.get_cached_token()
    if not token:
        authenticate(request)
    if request.GET.get('imageurl'):
        playlistId=createlist(request, request.GET.get('imageurl'))
        spotiURL='spotiPlayer?='+playlistId
        #Necesitamos que el urls.py nos redireccione bien.
        return redirect(spotiURL)
    if request.method == 'POST' and request.FILES['imagefile']:
        myfile = request.FILES['imagefile']
        fs = FileSystemStorage()
        imagen = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(imagen)
        url="."+uploaded_file_url
        playlistId=createlist(request, url)
        os.remove(url)
        spotiURL='spotiPlayer?='+playlistId
        #Necesitamos que el urls.py nos redireccione bien.
        return redirect(spotiURL)
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

@csrf_exempt
def spotiPlayer(request):
    return render(request, 'image2songs/spotiPlayer.html')