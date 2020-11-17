from rest_framework import serializers
from .models import Todo
# from users.serializers import UserSerializer

class TodoSerializer(serializers.ModelSerializer):

    # user = UserSerializer()

    class Meta:
        model = Todo
        fields = ('name', 'start_date', 'end_date', 'is_group', 'evidence_text', 'user')