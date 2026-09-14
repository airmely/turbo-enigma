from rest_framework.routers import DefaultRouter

from apps.users.rest.views import UserViewSet

app_name = "users"
router = DefaultRouter()

router.register(r"users", UserViewSet)

urlpatterns = router.urls
