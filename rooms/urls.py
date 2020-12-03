from . import views
from rest_framework.routers import DefaultRouter

app_name = 'rooms'
router = DefaultRouter()
router.register(r"", views.RoomViewSet)

urlpatterns = router.urls
