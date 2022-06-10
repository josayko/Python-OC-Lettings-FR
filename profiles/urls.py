from django.urls import path
from profiles.views import profiles_index, profile

urlpatterns = [
    path("", profiles_index, name="profiles_index"),
    path("<str:username>/", profile, name="profile"),
]