from django.contrib import admin
from django.urls import path
from dmr.openapi import build_schema
from dmr.openapi.views import OpenAPIJsonView, SwaggerView

from services.api import router as main_router

schema = build_schema(main_router)

urlpatterns = [
    main_router.to_urlpatterns(namespace="api"),
    path("admin/", admin.site.urls),
    path("docs/openapi.json/", OpenAPIJsonView.as_view(schema), name="openapi"),
    path("docs/swagger/", SwaggerView.as_view(schema), name="swagger"),
    # path("api/", include("services.api.balance.urls")),
    # path("api/", include("services.api.users.urls")),
]
