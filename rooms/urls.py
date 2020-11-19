from django.urls import path
from . import views

app_name = 'rooms'

urlpatterns = [path('',views.list_rooms),
               path('/<int:pk>/', views.SeeRoomViews.as_view())]