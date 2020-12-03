from rest_framework import permissions
from rest_framework import status
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from django.contrib.auth import login
from .serializers import UserSerializer
from .permissions import IsOwner
import requests
from django.shortcuts import redirect
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
        return [p() for p in permission_classes]

    @action(detail=True, methods=['get'])
    def messss(self, request, pk):
        print(pk)
        print(request.user)
        return Response(status=status.HTTP_200_OK)

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
        serializer = UserSerializer(user)

        return Response(serializer.data)

    def put(self, request):
        pass

def kakao_login(request):
    k_id = os.getenv('KAKAO_CLIENT_ID')
    r_uri = 'http://127.0.0.1:8001/api/v1/users/login/kakao/callback'
    return redirect(
        f"https://kauth.kakao.com/oauth/authorize?client_id={k_id}&redirect_uri={r_uri}&response_type=code"
    )

class KakaoException(Exception):
    pass

def kakao_callback(request):
    k_id = os.getenv('KAKAO_CLIENT_ID')
    r_uri = 'http://127.0.0.1:8001/api/v1/users/login/kakao/callback'
    try:
        user_token = request.GET.get("code")
        token_request = requests.get(
            f"https://kauth.kakao.com/oauth/token?grant_type=authorization_code&client_id={k_id}&redirect_uri={r_uri}&code={user_token}"
        )
        token_response_json = token_request.json()
        error = token_response_json.get("error", None)

        if error is not None:
            raise KakaoException("Can't get authorization code.")
        access_token = token_response_json.get("access_token")
        profile_request = requests.get(
            "https://kapi.kakao.com/v2/user/me",
            headers={"Authorization": f"Bearer {access_token}"},
        )
        profile_json = profile_request.json()
        new_id = profile_json.get("id")
        new_nickname = profile_json['properties']['nickname']
        try:
            user = User.objects.get(username=new_id)
        except User.DoesNotExist:
            user = User.objects.create(
                username = new_id,
                nickname = new_nickname,
                login_method = 'kakao'
            )
            user.set_unusable_password()
            user.save()
        login(request, user)
        return redirect('http://127.0.0.1:8001/api/v1/users/me/')
    except KakaoException as e:
        return redirect('http://127.0.0.1:8001/api/v1/')
