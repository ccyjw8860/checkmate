from django.db import models
from users.models import User
# Create your models here.

class Photo(models.Model):
    file = models.ImageField()
    room = models.ForeignKey(
        "rooms.Room", related_name="photos", on_delete=models.CASCADE
    )
    caption = models.CharField(max_length=140)

    def __str__(self):
        return self.room.title


class Room(models.Model):
    title = models.CharField(max_length=140)
    description = models.TextField()
    host = models.ForeignKey(User, on_delete=models.CASCADE, related_name='rooms')

    def __str__(self):
        return self.title