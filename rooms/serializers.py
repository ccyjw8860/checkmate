from rest_framework import serializers
from .models import Room
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
        fields = ('id','username', 'todos')

class RoomSerializer(serializers.ModelSerializer):
    users = RoomUserSerializer(many=True, read_only=True)

    class Meta:
        ordering = ['-id']
        model = Room
        fields = ('id','title', 'description', 'host', 'users')
        extra_kwargs = {'users':{'required':False}}

