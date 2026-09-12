from dmr.routing import Router

from services.api.auth.urls import router as auth_router
from services.api.balance.urls import router as balance_router

router = Router("api/v1/")

router.include(
    auth_router,
    namespace="auth",
    app_name="auth",
)

router.include(
    balance_router,
    namespace="balance",
    app_name="balance",
)
