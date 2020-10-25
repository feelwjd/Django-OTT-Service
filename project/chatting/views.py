from django.shortcuts import render, redirect, get_object_or_404
from streamming.models import StreammingNvideo
from account.models import Profile
from streamming.forms import VideoForm
from django.utils.safestring import mark_safe
import json
# Create your views here.
def room(request,nid,room_name):
    show = get_object_or_404(StreammingNvideo,pk=nid)
    nv = StreammingNvideo.objects.last()
    nvideos = nv.nvideo
    vid = str(nvideos)
    vid1 = vid.lstrip("b'")
    vid2 = vid1.strip("'")
    form = VideoForm(request.POST or None , request.FILES or None)
    return render(request,'room.html',{'nvideos':vid2, 'room_name_json': mark_safe(json.dumps(room_name))})

# def room(request,nid):
#     show = get_object_or_404(StreammingNvideo,pk=nid)
#     nv = StreammingNvideo.objects.last()
#     nvideos = nv.nvideo
#     vid = str(nvideos)
#     vid1 = vid.lstrip("b'")
#     vid2 = vid1.strip("'")
#     form = VideoForm(request.POST or None , request.FILES or None)
#     return render(request,'room.html',{'nvideos':vid2})

def password(request,nid):
    auser = Profile.objects.get(user)
    
    return render(request,'password.html')
