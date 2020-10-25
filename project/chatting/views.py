from django.shortcuts import render, redirect, get_object_or_404
from .models import StreammingNvideo
from .forms import VideoForm
# Create your views here.
def room(request,nid):
    show = get_object_or_404(StreammingNvideo,pk=nid)
    nv = StreammingNvideo.objects.last()
    nvideos = nv.nvideo
    vid = str(nvideos)
    vid1 = vid.lstrip("b'")
    vid2 = vid1.strip("'")
    form = VideoForm(request.POST or None , request.FILES or None)
    return render(request,'room.html',{'nvideos':vid2})

