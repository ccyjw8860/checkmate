from django.contrib import admin
from . import models
from django.utils.html import mark_safe
from rooms.models import Room

@admin.register(models.TodoPhoto)
class ToDoPhotoAdmin(admin.ModelAdmin):
    list_display = (
        '__str__',
        'get_todo_thumbnail'
    )

    def get_todo_thumbnail(self, obj):
        return mark_safe(f'<img width=50px height=50px src={obj.file.url}/>')

    get_todo_thumbnail.short_description = 'Todo Thumbnail'

class TodoPhotoInline(admin.TabularInline):
    model = models.TodoPhoto

@admin.register(models.Todo)
class TodoAdmin(admin.ModelAdmin):

    inlines = (TodoPhotoInline,)

    list_display = (
        "name",
        "start_date",
        "end_date",
        'is_group',
        'evidence_text',
        'users'
    )



