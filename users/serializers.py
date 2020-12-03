from rest_framework import serializers
from .models import User
from todos.serializers import TodoSerializer
from rooms.models import Room, RoomPhoto

"""
serializers는 JSON -> python dict, python dict -> JSON으로 변환하는 tool
"""

class UserRoomPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model= RoomPhoto
        fields = ('file',)

class UserRoomSerializer(serializers.ModelSerializer):
    room_photos = UserRoomPhotoSerializer(many=True, read_only=True)
    class Meta:
        model = Room
        fields = ('id', 'title', 'description', 'host','room_photos')


class UserSerializer(serializers.ModelSerializer):
    todos = TodoSerializer(many=True, read_only=True)
    rooms = UserRoomSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'nickname','todos', 'rooms')

class ChoiceField(serializers.ChoiceField):

    def to_representation(self, obj):
        if obj == '' and self.allow_blank:
            return obj
        return self._choices[obj]

    def to_internal_value(self, data):
        # To support inserts with the value
        if data == '' and self.allow_blank:
            return ''

        for key, val in self._choices.items():
            if val == data:
                return key
        self.fail('invalid_choice', input=data)

class MakeUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'password'
        )

    def create(self, validated_data):
        password = validated_data.get('password')
        user = super().create(validated_data)
        user.set_password(password)
        user.save()
        return user

    def update(self, instance, validated_data):
        pass