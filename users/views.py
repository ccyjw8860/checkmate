from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import User
from .serializers import UserSerializer

@api_view(['GET'])
def list_users(request):
    users = User.objects.all()
    serialized_users = UserSerializer(users, many=True)
    return Response(data = serialized_users.data)

# Create your views here.
