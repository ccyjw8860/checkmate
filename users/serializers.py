from rest_framework import serializers
from .models import User
from todos.serializers import TodoSerializer
from rooms.models import Room

"""
serializers는 JSON -> python dict, python dict -> JSON으로 변환하는 tool
"""

class UserRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    todos = TodoSerializer(many=True, read_only=True)
    rooms = UserRoomSerializer(many=True, read_only=True)
    class Meta:
        model = User
        fields = ('id','username', 'email', 'gender', 'birthdate', 'todos', 'rooms')

