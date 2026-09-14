from drf_yasg import openapi
from drf_yasg.generators import OpenAPISchemaGenerator
from drf_yasg.views import get_schema_view as default_get_schema_view
from rest_framework.permissions import AllowAny


class _CustomSchemaGenerator(OpenAPISchemaGenerator):
    def get_schema(self, request=None, public=False):
        schema = super().get_schema(request, public)
        schema.schemes = [
            "http",
            "https",
        ]
        return schema


def get_schema_view(title: str, version: str):
    return default_get_schema_view(
        openapi.Info(title=title, default_version=version),
        public=True,
        generator_class=_CustomSchemaGenerator,
        permission_classes=(AllowAny,),  # noqa
    )


schema_view = get_schema_view(title="Balance System", version="0.0.1")
