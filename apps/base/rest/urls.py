from django.urls import path

from apps.base.openapi_schema_generator import schema_view

urlpatterns = [
    path(
        "swagger/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
]
