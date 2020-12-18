from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

app_name = 'users'
router = DefaultRouter()
router.register(r"", views.UserViewSet)

# extra_patterns = [path('login/kakao/', views.kakao_login),
#                   path('login/kakao/callback/', views.kakao_callback)]

urlpatterns = router.urls