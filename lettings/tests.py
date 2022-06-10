from django.test import TestCase
from django.urls import reverse

from .models import Address, Letting


class LettingsPageTests(TestCase):
    def setUp(self):
        self.address = Address.objects.create(
            number="1",
            street="Avenue de l'Opéra",
            city="Paris",
            state="Ile-De-France",
            zip_code="75008",
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
