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

def detail1(request):
    nv = StreammingNvideo.objects.get(pk=4)
    nvideos = nv.nvideo
    vid = str(nvideos)
    vid1 = vid.lstrip("b'")
    vid2 = vid1.strip("'")
    form = VideoForm(request.POST or None , request.FILES or None)
    if form.is_valid():
        form.save()
    return render(request, 'detail1.html',{'nvideos':vid2,'form':form})

def book1(request):
    nv = StreammingNvideo.objects.last()
    nvideos = nv.nvideo
    vid = str(nvideos)
    vid1 = vid.lstrip("b'")
    vid2 = vid1.strip("'")
    form = VideoForm(request.POST or None , request.FILES or None)
    if form.is_valid():
        form.save()
    return render(request, 'book1.html',{'nvideos':vid2})

def index(request):
    return render(request, 'index.html')

def mypage(request):
    return render(request,'mypage.html')

def book2(request):
    return render(request, 'book2.html')

def book3(request):
    return render(request, 'book3.html')

def book4(request):
    return render(request, 'book4.html')

def book5(request):
    return render(request, 'book5.html')

def detail2(request):
    nv = StreammingNvideo.objects.get(pk=1)
    nvideos = nv.nvideo
    vid = str(nvideos)
    vid1 = vid.lstrip("b'")
    vid2 = vid1.strip("'")
    return render(request, 'detail2.html',{'nvideos':vid2})

def detail3(request):
    nv = StreammingNvideo.objects.get(pk=2)
    nvideos = nv.nvideo
    vid = str(nvideos)
    vid1 = vid.lstrip("b'")
    vid2 = vid1.strip("'")
    return render(request, 'detail3.html',{'nvideos':vid2})

def detail4(request):
    nv = StreammingNvideo.objects.get(pk=5)
    nvideos = nv.nvideo
    vid = str(nvideos)
    vid1 = vid.lstrip("b'")
    vid2 = vid1.strip("'")
    return render(request, 'detail4.html',{'nvideos':vid2})

def detail5(request):
    nv = StreammingNvideo.objects.get(pk=5)
    nvideos = nv.nvideo
    vid = str(nvideos)
    vid1 = vid.lstrip("b'")
    vid2 = vid1.strip("'")
    return render(request, 'detail5.html',{'nvideos':vid2})

def room(request):
    nv = StreammingNvideo.objects.last()
    nvideos = nv.nvideo
    vid = str(nvideos)
    vid1 = vid.lstrip("b'")
    vid2 = vid1.strip("'")
    form = VideoForm(request.POST or None , request.FILES or None)
    return render(request,'room.html',{'nvideos':vid2})