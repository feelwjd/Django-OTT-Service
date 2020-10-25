from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static




urlpatterns = [
    path('video',views.video,name='video'),
    path('detail1',views.detail1,name='detail1'),
    path('mypage',views.mypage,name='mypage'),
    path('',views.index,name='index'),
    path('book1', views.book1, name='book1'),
    path('book2', views.book2, name='book2'),
    path('book3', views.book3, name='book3'),
    path('book4', views.book4, name='book4'),
    path('book5', views.book5, name='book5'),
    path('detail2', views.detail2, name='detail2'),
    path('detail3', views.detail3, name='detail3'),
    path('detail4', views.detail4, name='detail4'),
    path('detail5', views.detail5, name='detail5'),
    path('room',views.room,name='room')
]