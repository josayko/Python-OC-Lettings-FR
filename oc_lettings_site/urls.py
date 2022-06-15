from django.contrib import admin
from django.urls import include, path

from . import views


def sentry_error(request):
    division_by_zero = 1 / 0
    return division_by_zero


urlpatterns = [
    path("sentry-debug/", sentry_error),
    path("", views.index, name="index"),
    path("lettings/", include("lettings.urls")),
    path("profiles/", include("profiles.urls")),
    path("admin/", admin.site.urls),
]
