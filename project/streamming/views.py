from django.shortcuts import render, redirect, get_object_or_404
from .models import StreammingNvideo
from .forms import VideoForm
# Create your views here.
def video(request):
    nv = StreammingNvideo.objects.last()
    nvideos = nv.nvideo
    vid = str(nvideos)
    vid1 = vid.lstrip("b'")
    vid2 = vid1.strip("'")
    form = VideoForm(request.POST or None , request.FILES or None)
    if form.is_valid():
        form.save()
    return render(request, 'video.html',{'nvideos':vid2,'form':form})