from django.urls import path
from . import views
from streamming import urls
urlpatterns = [
    path('room',views.room,name='room'),
    path('password',views.password,name='password'),
    path('checkpw',views.checkpw,name='checkpw')
]
