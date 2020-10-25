from django.urls import path
from django.contrib.auth.decorators import login_required
from . import views

urlpatterns = [
    path('signin',views.signin,name='login'),
    path('signup',views.signup,name='signup'),
    path('logout',views.logout,name='logout'),
]
