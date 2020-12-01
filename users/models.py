from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _

from .managers import CustomUserManager

class User(AbstractUser):
    username = models.CharField(max_length=50, unique=True)
    login_method = models.CharField(max_length=5, default='kakao')
    rooms = models.ManyToManyField('rooms.Room', related_name='users')

    def __str__(self):
        return self.username
