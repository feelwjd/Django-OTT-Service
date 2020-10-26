from django.shortcuts import render, redirect, get_object_or_404
from streamming.models import StreammingNvideo , Checkout
from account.models import Profile
from .forms import VideoForm
from django.contrib import messages
from django.utils.safestring import mark_safe
import json

# Create your views here.
def room(request):
    auser = request.user
    anid = auser.username
    videonum = Checkout.objects.filter(user_id=anid).last()
    imagenum = videonum.nid
    nv = StreammingNvideo.objects.get(pk=imagenum)
    nvideos = nv.nvideo
    vid = str(nvideos)
    vid1 = vid.lstrip("b'")
    vid2 = vid1.strip("'")
    form = VideoForm(request.POST or None , request.FILES or None)
    return render(request,'room.html',{'nvideos':vid2})

# def room(request,nid):
#     show = get_object_or_404(StreammingNvideo,pk=nid)
#     nv = StreammingNvideo.objects.last()
#     nvideos = nv.nvideo
#     vid = str(nvideos)
#     vid1 = vid.lstrip("b'")
#     vid2 = vid1.strip("'")
#     form = VideoForm(request.POST or None , request.FILES or None)
#     return render(request,'room.html',{'nvideos':vid2})

def password(request):
    return render(request,'password.html')

def checkpw(request):
    auser = request.user
    anid = auser.username
    videonum = Checkout.objects.filter(user_id=anid).last()
    ticket = videonum.num
    inpw = request.POST["inpw"]
    if (ticket == inpw):
        return redirect('room')
    else:
        messages.info(request, '비밀번호가 틀렸습니다!')
        return render(request,'password.html')
    return render(request,'password.html')
