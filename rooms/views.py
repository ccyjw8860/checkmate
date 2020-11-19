from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.response import Response
from .models import Room
from .serializers import RoomSerializer, OneRoomSerializer

@api_view(['GET'])
def list_rooms(request):
    room = Room.objects.all()
    serialized_room = RoomSerializer(room, many=True)
    return Response(data = serialized_room.data)

class SeeRoomViews(RetrieveAPIView):
    queryset = Room.objects.all()
    serializer_class = OneRoomSerializer