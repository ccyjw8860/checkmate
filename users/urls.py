from django.urls import path, include
from . import views
from allauth.account.views import confirm_email
from django.conf.urls import url
from django.contrib import admin
from .views import kakao_callback, kakao_login, KakaoToDjangoLogin

app_name = 'users'

urlpatterns = [path('/me/',views.MeView.as_view()),
               path('/<int:pk>/', views.UserView.as_view()),
               url(r'^rest-auth/', include('rest_auth.urls')),
               url(r'^rest-auth/registration/', include('rest_auth.registration.urls')),
               url(r'^account/', include('allauth.urls')),
               url(r'^accounts-rest/registration/account-confirm-email/(?P<key>.+)/$', confirm_email, name='account_confirm_email'),
               path('/login/kakao/', kakao_login),
               path('/login/kakao/callback/', kakao_callback),
               path('/login/kakao/todjango', KakaoToDjangoLogin.as_view()),
               ]