from dmr.routing import Router, path
from dmr.security.jwt.views import ObtainTokensSyncController

router = Router(
    "auth/",
    [
        path(
            "/access-token/",
            ObtainTokensSyncController.as_view(),
            name="auth-access-token",
        ),
    ],
    tags=["Authentication"],
)
