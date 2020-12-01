from rest_framework.generics import RetrieveAPIView, ListAPIView
from rest_framework.views import APIView, View
from rest_framework import status
from rest_framework.response import Response

from .models import User
from .serializers import UserSerializer, MakeUserSerializer
from dj_rest_auth.registration.views import SocialLoginView
from allauth.socialaccount.providers.kakao.views import KakaoOAuth2Adapter
from allauth.socialaccount.providers.kakao import views as kakao_views
from allauth.socialaccount.providers.naver import views as naver_views
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
import requests
from django.shortcuts import redirect
from .models import User
import os, json
from dotenv import load_dotenv

load_dotenv()

BASE_DIR = os.path.dirname(os.path.dirname(__file__))   # 프로젝트/accounts

with open(os.path.join(BASE_DIR, 'config\secret.json'), 'rb') as secret_file:
    secrets = json.load(secret_file)

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
        print(user)
        print(vars(request))
        # print(user.is_authenticated)
        serializer = UserSerializer(user)
        # print(dir(serializer))

        return Response(serializer.data)

    def put(self, request):
        pass


def kakao_login(request):
    k_id = os.getenv('KAKAO_CLIENT_ID')
    r_uri = 'http://127.0.0.1:8001/api/v1/users/login/kakao/callback'
    return redirect(
        f"https://kauth.kakao.com/oauth/authorize?client_id={k_id}&redirect_uri={r_uri}&response_type=code"
    )

def kakao_callback(request):
    k_id = os.getenv('KAKAO_CLIENT_ID')
    r_uri = 'http://127.0.0.1:8001/api/v1/users/login/kakao/callback'
    user_token = request.GET.get("code")
    print('===================user_token===================')
    print(user_token)
    print('===================user_token===================')
    token_request = requests.get(
        f"https://kauth.kakao.com/oauth/token?grant_type=authorization_code&client_id={k_id}&redirect_uri={r_uri}&code={user_token}"
    )
    token_response_json = token_request.json()
    error = token_response_json.get("error", None)
    print('===================token_response===================')
    print(token_response_json)
    print('===================token_response===================')
    if error is not None:
        return Response(status.HTTP_400_BAD_REQUEST)
    else:
        access_token = token_response_json.get("access_token")
        profile_request = requests.post(
            "https://kapi.kakao.com/v2/user/me",
            headers={"Authorization": f"Bearer {access_token}"},
        )
        profile_json = profile_request.json()
        new_id = profile_json.get("id")
        new_nickname = profile_json['properties']['nickname']
        new_username = f'{new_id}_{new_nickname}'
        try:
            user_check = User.objects.get(username=new_id)
            print('success')
        except User.DoesNotExist:
            print('failed')
            pass
        # if user_check is None:

        print('-------------profile---------------')
        print(profile_json)
        print('-------------profile---------------')
        username = str(profile_json.get('id'))

        # user_in_db = User.objects.get(username=username)
        data = {'code': user_token, 'access_token': access_token}
        accept = requests.post(
            f"http://127.0.0.1:8001/api/v1/users/login/kakao/todjango", data=data
        )
        accept_json = accept.json()
        print('-------------accept_json---------------')
        print(accept_json)
        print('-------------accept_json---------------')
        return redirect('http://127.0.0.1:8001/api/v1/users/me/')
        # 이미 kakao로 가입된 유저라면
        # if user_in_db is not None:
        #     # 서비스에 rest-auth 로그인
        #     data = {'code': user_token, 'access_token': access_token}
        #     accept = requests.post(
        #         f"http://127.0.0.1:8000/account/login/kakao/todjango", data=data
        #     )
        #     accept_json = accept.json()
        #     print(accept_json)
        # else:
        #     pass
                # accept_jwt = accept_json.get("token")
                #
                # # 프로필 정보 업데이트
                # User.objects.filter(username=username).update(
                #                                         login_method='kakao',
                #                                         profile_image=profile_image,
                #                                         is_active=True
                #                                         )
        # except User.DoesNotExist:
        #     # 서비스에 rest-auth 로그인
        #     data = {'code': user_token, 'access_token': access_token}
        #     accept = requests.post(
        #         f"http://127.0.0.1:8000/account/login/kakao/todjango", data=data
        #     )
        #     accept_json = accept.json()
        #     accept_jwt = accept_json.get("token")
        #
        #     User.objects.filter(email=email).update(realname=nickname,
        #                                             email=email,
        #                                             user_type='kakao',
        #                                             profile_image=profile_image,
        #                                             is_active=True
        #                                             )
        # return redirect("http://127.0.0.1:8000/")  # 메인 페이지


class KakaoToDjangoLogin(SocialLoginView):
    adapter_class = KakaoOAuth2Adapter
    callback_url = 'http://127.0.0.1:8001/api/v1/users/login/kakao/callback'
    client_class = OAuth2Client