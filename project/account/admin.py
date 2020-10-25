from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import Profile

# Register your models here.
class ProfileInline(admin.StackedInline): 
    model = Profile
    con_delete = False                    # 프로필을 아예 없앨 수 없게 하는 속성


class CustomUserAdmin(UserAdmin):
    inlines = (ProfileInline,)

# 기존의 User의 등록을 취소했다가 User와 ProfileInline을 붙임.
admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)