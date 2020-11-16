from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models

@admin.register(models.User) #admin pannel에서 user를 보여줄거다. user를 컨트롤하는 class는 CustomUserAdmin이다
class CustomUserAdmin(UserAdmin):

    """Custom User Admin"""
    fieldsets = ('username', 'email', 'gender', 'birthdate')

    list_display = (
        'username',
        'email',
        'gender',
        'birthdate'
    )