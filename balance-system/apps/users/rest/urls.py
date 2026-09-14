from apps.users.rest.views import UserViewSet
from rest_framework.routers import DefaultRouter

app_name = "users"
router = DefaultRouter()

router.register(r"users", UserViewSet)

urlpatterns = router.urls
