from django.test import TestCase, Client
from django.urls import reverse
from .models import Media, Emprunteur, Emprunt
from django.utils import timezone

class MediaTestCase(TestCase):
    def setUp(self):
        self.media = Media.objects.create(titre="Test Livre", type="livre", disponible=True)

    def test_media_creation(self):
        self.assertEqual(self.media.titre, "Test Livre")
        self.assertTrue(self.media.disponible)

class EmpruntTestCase(TestCase):
    def setUp(self):
        self.emprunteur = Emprunteur.objects.create(
            nom="Test", prenom="Utilisateur", email="test@example.com", telephone="1234567890"
        )
        self.media = Media.objects.create(titre="Livre Test", type="livre", disponible=True)
        self.emprunt = Emprunt.objects.create(media=self.media, emprunteur=self.emprunteur, date_emprunt=timezone.now())

    def test_emprunt_creation(self):
        self.assertEqual(self.emprunt.media.titre, "Livre Test")
        self.assertEqual(self.emprunt.emprunteur.nom, "Test")

class PagesAccessibilityTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_homepage_access(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)

    def test_connexion_page_access(self):
        response = self.client.get(reverse("connexion"))
        self.assertEqual(response.status_code, 200)
