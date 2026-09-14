from apps.base.openapi_schema_generator import schema_view
from django.urls import include, path

urlpatterns = [
    path("auth/", include("djoser.urls.authtoken")),
    path(
        "swagger/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
]
