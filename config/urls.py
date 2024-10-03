from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("apps.base.rest.urls")),
    path("api/", include("apps.users.rest.urls")),
]
