from django.urls import path
from . import views

urlpatterns = [
    # path('room/<int:nid>',views.room,name='room'),
    # path('password/<int:nid>',views.password,name='password'),
    url(r'^$', views.index, name='index'),
    url(r'^(?P<room_name>[^/]+)/$', views.room, name='room'),
]
