from django.db import models
# Create your models here.

class RoomPhoto(models.Model):
    file = models.ImageField(upload_to='room_photos')
    room = models.ForeignKey(
        "rooms.Room", related_name="room_photos", on_delete=models.CASCADE
    )
    caption = models.CharField(max_length=140)

    def __str__(self):
        return self.room.title


class Room(models.Model):
    title = models.CharField(max_length=140)
    description = models.TextField()
    host = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='roomhost')

    def __str__(self):
        return self.title
