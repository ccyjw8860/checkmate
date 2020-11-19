from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [path('/',views.UsersView.as_view()),
               path('/<int:pk>/', views.UserView.as_view())]