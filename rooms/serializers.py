from rest_framework import serializers
from .models import Room, RoomPhoto
from users.models import User
from todos.models import Todo

class RoomTodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = '__all__'

class RoomUserSerializer(serializers.ModelSerializer):
    todos = RoomTodoSerializer(many=True, read_only=True)
    class Meta:
        model = User
        fields = ('id', 'username','gender', 'todos')

class RoomPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model=RoomPhoto
        fields = ('file',)

class RoomSerializer(serializers.ModelSerializer):
    users = RoomUserSerializer(many=True, read_only=True)
    photos = RoomPhotoSerializer(many=True, read_only=True)
    class Meta:
        ordering = ['-pk']
        model = Room
        fields = ('pk','title', 'description', 'host', 'photos', 'users')
        extra_kwargs = {'users':{'required':False}}

class OneRoomSerializer(serializers.ModelSerializer):
    users = RoomUserSerializer(many=True, read_only=True)
    photos = RoomPhotoSerializer(many=True, read_only=True)
    class Meta:
        model = Room
        fields = ('title', 'description', 'host', 'photos', 'users')

class UserRoomSerializer(serializers.ModelSerializer):
    photos = RoomPhotoSerializer(many=True, read_only=True)
    class Meta:
        model = Room
        fields = ('title', 'description', 'host', 'photos')