from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Todo
from .serializers import TodoSerializer

@api_view(['GET'])
def list_todos(request):
    todo = Todo.objects.all()
    serialized_todo = TodoSerializer(todo, many=True)
    return Response(data = serialized_todo.data)

# Create your views here.
