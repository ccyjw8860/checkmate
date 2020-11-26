from django.urls import path, include
from . import views
from allauth.account.views import confirm_email
from django.conf.urls import url
from django.contrib import admin
from .views import KakaoToDjangoLogin


app_name = 'users'

urlpatterns = [path('/me/',views.MeView.as_view()),
               path('/<int:pk>/', views.UserView.as_view()),
               path('/login/kakao/', views.kakao_login),
               path('/login/kakao/callback/', views.kakao_callback),
               path('/login/kakao/todjango', KakaoToDjangoLogin.as_view()),
               ]