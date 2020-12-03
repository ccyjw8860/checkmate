from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions
from .serializers import TodoSerializer
from .models import Todo
from .permissions import IsOwner

class TodoViewSet(ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

    def get_permissions(self):
        if self.action == 'retrieve':
            permission_classes = [permissions.AllowAny]
        elif self.action == 'list':
            permission_classes = [permissions.IsAdminUser]
        elif self.action == 'create':
            permission_classes = [permissions.IsAuthenticated]
        else:
            permission_classes = [IsOwner]
        return [permission() for permission in permission_classes]