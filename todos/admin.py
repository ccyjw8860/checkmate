from django.contrib import admin
from . import models

@admin.register(models.Todo)
class TodoAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "start_date",
        "end_date",
        'is_group',
        'evidence_text',
        'user'
    )


@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):
    pass
