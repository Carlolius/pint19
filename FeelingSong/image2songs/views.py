from django.shortcuts import render
from django.http import HttpResponse
from image2songs.models import UserData, Feeling

# Create your views here.

def index(request):
    userData_list=UserData.objects.all()
    context={'userData_list':userData_list}
    return render(request,'image2songs/index.html', context)

def detail(request,userData_id):
    f=UserData.objects.get(id=userData_id)
    image2songs_list=f.feeling_set.all()
    context={'f':f,'image2songs_list':image2songs_list}
    return render(request,'image2songs/userData_detail.html', context)
