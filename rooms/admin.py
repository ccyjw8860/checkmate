from django.contrib import admin
from . import models

@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):

    list_display = (
        'title',
        'host'
    )



@admin.register(models.RoomPhoto)
class PhotoAdmin(admin.ModelAdmin):
    pass