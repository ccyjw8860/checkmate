from django.contrib import admin
from . import models
from django.utils.html import mark_safe

class RoomPhotoInline(admin.TabularInline):
    model = models.RoomPhoto

@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):

    inlines = (RoomPhotoInline,)

    list_display = (
        'title',
        'host',
    )

@admin.register(models.RoomPhoto)
class RoomPhotoAdmin(admin.ModelAdmin):
    list_display = (
        '__str__',
        'get_room_thumbnail'
    )

    def get_room_thumbnail(self,obj):
        return mark_safe(f'<img width=50px height=50px src={obj.file.url}/>')

    get_room_thumbnail.short_description = 'Room Thumbnail'