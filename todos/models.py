from django.db import models
from django.urls import reverse

# Create your models here.

class Photo(models.Model):
    """ Photo model definition"""

    caption = models.CharField(max_length=80)
    file = models.ImageField(upload_to='room_photos')
    todo = models.ForeignKey('todo', on_delete=models.CASCADE, related_name='photos')

    def __str__(self):
        return self.todo.name

class Todo(models.Model):

    """ Room Model Definition"""

    name = models.CharField(max_length=140)
    date = models.DateField()
    term = models.IntegerField()
    is_group = models.BooleanField(default=False)
    evidence_text = models.CharField(max_length=300)

    def __str__(self):
        return self.name
