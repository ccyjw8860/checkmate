from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from .serializers import UserSerializer, UserRoomSerializer
from .permissions import IsOwner
from rooms.serializers import OneRoomSerializer
import requests

from .models import User
import os, json
from dotenv import load_dotenv

load_dotenv()
BASE_DIR = os.path.dirname(os.path.dirname(__file__))   # 프로젝트/accounts
with open(os.path.join(BASE_DIR, 'config\secret.json'), 'rb') as secret_file:
    secrets = json.load(secret_file)

class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        if self.action == 'list':
            permission_classes = [permissions.IsAdminUser]
        elif self.action == 'retrieve' or self.action == 'create':
            permission_classes = [permissions.IsAuthenticated]
        else:
            permission_classes = [IsOwner]
        return [permission() for permission in permission_classes]

    @action(detail=False, methods=['get', 'put'])
    def me(self, request):
        user = request.user
        serializer = UserSerializer(user)

        return Response(serializer.data)

    @action(detail=True)
    def rooms(self, request, pk):
        user = self.get_object()
        serializer = OneRoomSerializer(user.rooms.all(), many=True).data
        return Response(serializer)


