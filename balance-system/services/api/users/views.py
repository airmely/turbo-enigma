from djoser.serializers import UserDeleteSerializer
from djoser.views import UserViewSet as DjoserUserViewSet
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.decorators import action


class UserViewSet(DjoserUserViewSet):
    @swagger_auto_schema(
        method="delete",
        request_body=UserDeleteSerializer,
        responses={status.HTTP_204_NO_CONTENT: "No Content"},
    )
    @action(
        detail=False,
        methods=["get", "put", "patch", "delete"],
        url_path="me",
    )
    def me(self, request, *args, **kwargs):
        """This is done so that it is possible to enter current_password in swagger."""
        return super().me(request, *args, **kwargs)
