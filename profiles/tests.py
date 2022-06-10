from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from .models import Profile


class TestProfiles(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="josayko", password="aBcd123", email="josayko@orangecounty.com"
        )
        self.profile = Profile.objects.create(
            user=self.user,
            favorite_city="Tokyo",
        )

    def test_profile_index(self):
        response = self.client.get(reverse("profiles:profiles_index"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "profiles/index.html")
        self.assertIn(b"<title>Profiles</title>", response.content)

    def test_profile_detail(self):
        response = self.client.get(reverse("profiles:profile", args=["josayko"]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "profiles/profile.html")

    def test_profile_model(self):
        assert str(self.profile) == f"{self.profile.user.username}"
