from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("apps.balance.rest.urls")),
    path("api/", include("apps.base.rest.urls")),
    path("api/", include("apps.users.rest.urls")),
]
