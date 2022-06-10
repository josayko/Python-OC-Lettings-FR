from django.test import TestCase
from django.urls import reverse

from .models import Address, Letting


class TestLettings(TestCase):
    def setUp(self):
        self.address = Address.objects.create(
            number="1",
            street="Avenue de l'Opéra",
            city="Paris",
            state="Ile-De-France",
            zip_code="75001",
            country_iso_code="FR",
        )
        self.letting = Letting.objects.create(
            title="Opéra Garnier",
            address=self.address,
        )

    def test_lettings_index(self):
        response = self.client.get(reverse("lettings:lettings_index"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "lettings/index.html")
        self.assertIn(b"<title>Lettings</title>", response.content)

    def test_lettings_detail(self):
        response = self.client.get(reverse("lettings:letting", args=[1]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "lettings/letting.html")

    def test_lettings_model(self):
        assert str(self.address) == f"{self.address.number} {self.address.street}"
        assert str(self.letting) == f"{self.letting.title}"
