from django.shortcuts import render, redirect, get_object_or_404
from .models import StreammingNvideo,Checkout
from account.models import Profile , User
from .forms import VideoForm
import account.views
from django.contrib.auth.decorators import login_required
import string, random


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
    nv = StreammingNvideo.objects.get(pk=4)
    nvideos = nv.nvideo
    vid = str(nvideos)
    vid1 = vid.lstrip("b'")
    vid2 = vid1.strip("'")
    form = VideoForm(request.POST or None , request.FILES or None)
    if form.is_valid():
        form.save()
    vcode = 4
    return render(request, 'book1.html',{'nvideos':vid2,'vcode':vcode})

def index(request):
    return render(request, 'index.html')

@login_required
def mypage(request):
    auser = request.user
    anid = auser.username
    videonum = Checkout.objects.filter(user_id=anid).last()
    imagenum = videonum.nid
    timage = StreammingNvideo.objects.get(pk=imagenum)
    tick1 = str(timage.nimage)
    tick2 = tick1.lstrip("b'")
    ticket = tick2.strip("'")
    ticketai = videonum.num
    return render(request,'mypage.html',{'id':anid,'ticket':ticket,'code':ticketai})

def book2(request):
    nv = StreammingNvideo.objects.get(pk=1)
    nvideos = nv.nvideo
    vid = str(nvideos)
    vid1 = vid.lstrip("b'")
    vid2 = vid1.strip("'")
    return render(request, 'book2.html',{'nvideos':vid2})

def book3(request):
    nv = StreammingNvideo.objects.get(pk=2)
    nvideos = nv.nvideo
    vid = str(nvideos)
    vid1 = vid.lstrip("b'")
    vid2 = vid1.strip("'")
    return render(request, 'book3.html',{'nvideos':vid2})

def book4(request):
    nv = StreammingNvideo.objects.get(pk=5)
    nvideos = nv.nvideo
    vid = str(nvideos)
    vid1 = vid.lstrip("b'")
    vid2 = vid1.strip("'")
    return render(request, 'book4.html',{'nvideos':vid2})

def book5(request):
    nv = StreammingNvideo.objects.get(pk=3)
    nvideos = nv.nvideo
    vid = str(nvideos)
    vid1 = vid.lstrip("b'")
    vid2 = vid1.strip("'")
    return render(request, 'book5.html',{'nvideos':vid2})

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
    nv = StreammingNvideo.objects.get(pk=3)
    nvideos = nv.nvideo
    vid = str(nvideos)
    vid1 = vid.lstrip("b'")
    vid2 = vid1.strip("'")
    return render(request, 'detail5.html',{'nvideos':vid2})

def checkout(request):
    _Length = 10
    string_pool =string.ascii_letters
    result = ""
    for i in range(_Length):
        result += random.choice(string_pool)
    auser = request.user
    userid = auser.username
    vcode = request.POST['nid']
    getmv = StreammingNvideo.objects.get(pk=vcode)
    getlog = Checkout()
    getlog.user_id = userid
    getlog.nid = getmv.nid
    getlog.num = result
    getlog.save()
    return redirect('mypage')

def jindex(request):
    return render(request,'jindex.html')