from django.urls import include, path

from apps.base.openapi_schema_generator import schema_view

urlpatterns = [
    path("auth/", include("djoser.urls.authtoken")),
    path(
        "swagger/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
]
