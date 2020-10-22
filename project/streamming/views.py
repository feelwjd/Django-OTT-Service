from django.shortcuts import render, redirect, get_object_or_404
from .models import StreammingNvideo
from .forms import VideoForm
# Create your views here.
def video(request):
    nv = StreammingNvideo.objects.last()
    nvideos = nv.nvideo

    
     
    return render(request, 'video.html',{'nvideos':nvideos})