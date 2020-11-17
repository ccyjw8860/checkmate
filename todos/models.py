from django.db import models
from django.urls import reverse
from users import models as user_model

# Create your models here.

class Photo(models.Model):
    """ Photo model definition"""

    discription = models.TextField(default='')
    file = models.ImageField(upload_to='evidence_photos')
    todo = models.ForeignKey('todo', on_delete=models.CASCADE, related_name='photos')

    def __str__(self):
        return self.todo.name

class Todo(models.Model):

    """ Room Model Definition"""
    name = models.CharField(max_length=140)
    start_date = models.DateField(default=False)
    end_date = models.DateField(default=False)
    is_group = models.BooleanField(default=False)
    evidence_text = models.CharField(max_length=300, blank=True)
    user = models.ForeignKey(user_model.User, on_delete=models.CASCADE, related_name='todos')

    def __str__(self):
        return self.name