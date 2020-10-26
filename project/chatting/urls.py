from django.urls import path
from django.conf.urls import url
from . import views
from streamming import urls
urlpatterns = [
<<<<<<< HEAD
    path('room',views.room,name='room'),
    path('password',views.password,name='password'),
    path('checkpw',views.checkpw,name='checkpw')
=======
    # path('room/<int:nid>',views.room,name='room'),
    # path('password/<int:nid>',views.password,name='password'),
    url(r'^$', views.password, name='password'),
    url(r'^(?P<room_name>[^/]+)/$', views.room, name='room'),
>>>>>>> 618adf8c68e55a26d90f8539e74ce0ced1ebcb4f
]
