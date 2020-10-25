from django.urls import path
import streamming.views

urlpatterns = [
    path('', streamming.views.index, name='index'),
    path('book/', streamming.views.book, name='book'),
    path('book2/', streamming.views.book2, name='book2'),
    path('book3/', streamming.views.book3, name='book3'),
    path('book4/', streamming.views.book4, name='book4'),
    path('book5/', streamming.views.book5, name='book5'),
    path('detail/', streamming.views.detail, name='detail'),
    path('detail2/', streamming.views.detail2, name='detail2'),
    path('detail3/', streamming.views.detail3, name='detail3'),
    path('detail4/', streamming.views.detail4, name='detail4'),
    path('detail5/', streamming.views.detail5, name='detail5'),
]
