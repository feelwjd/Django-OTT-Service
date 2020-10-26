from django.urls import path
from django.conf.urls import url
from . import views
from streamming import urls
urlpatterns = [
    path('room',views.room,name='room'),
    path('password',views.password,name='password'),
    # url(r'^$', views.password, name='password'),
    # url(r'^(?P<room_name>[^/]+)/$', views.room, name='room'),
    path('checkpw',views.checkpw,name='checkpw'),
]

