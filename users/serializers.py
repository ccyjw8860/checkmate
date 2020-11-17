from rest_framework import serializers
from .models import User
from rooms.serializers import RoomSerializer


"""
serializers는 JSON -> python dict, python dict -> JSON으로 변환하는 tool
"""

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username', 'email', 'gender', 'birthdate', 'enrolled')
