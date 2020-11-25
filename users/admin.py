from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models

@admin.register(models.User) #admin pannel에서 user를 보여줄거다. user를 컨트롤하는 class는 CustomUserAdmin이다
class CustomUserAdmin(UserAdmin):

    """Custom User Admin"""

    fieldsets = UserAdmin.fieldsets + (
        ("Custom Profile", {"fields": ('date_of_birth', 'rooms')},),
    )

    list_display = (
        'email',
        'date_of_birth',
    )

    list_filter = ()
