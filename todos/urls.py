from . import views
from rest_framework.routers import DefaultRouter

app_name = 'todos'
router = DefaultRouter()
router.register(r"", views.TodoViewSet)

urlpatterns = router.urls