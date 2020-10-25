from django.urls import path
from . import views

urlpatterns = [
    path('room/<int:nid>',views.room,name='room')
]
