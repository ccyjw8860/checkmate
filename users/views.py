from rest_framework.generics import RetrieveAPIView, ListAPIView
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .models import User
from .serializers import UserSerializer, MakeUserSerializer


class UsersView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserView(APIView):
    def get_object(self, pk):
        try:
            user = User.objects.get(pk=pk)
            return user
        except User.DoesNotExist:
            return None

    def get(self, request, pk):
        user = self.get_object(pk)
        if user is not None:
            serializer = UserSerializer(user).data
            return Response(serializer)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self,request, pk):
        owner_user = self.get_object(pk)
        request_user = request.user
        if owner_user == request_user:
            owner_user.delete()
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_403_FORBIDDEN)

class MeView(APIView):
    def get(self, request):
        user = request.user
        print(request)
        # print(user.is_authenticated)
        serializer = UserSerializer(user)
        # print(dir(serializer))

        return Response(serializer.data)

    def put(self, request):
        pass