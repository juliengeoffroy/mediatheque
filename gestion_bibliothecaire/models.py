from django.db import models
from django.utils import timezone
from datetime import timedelta

class Emprunteur(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    adresse = models.TextField(max_length=255, blank=True)
    email = models.EmailField()
    telephone = models.CharField(max_length=20)
    bloque = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.prenom} {self.nom}"

class Media(models.Model):
    TYPE_CHOICES = [
        ('livre', 'Livre'),
        ('dvd', 'DVD'),
        ('cd', 'CD'),
        ('jeu', 'Jeu de plateau'),
    ]
    titre = models.CharField(max_length=100)
    type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    auteur = models.CharField(max_length=100, blank=True, null=True)
    disponible = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.titre} ({self.get_type_display()})"

class Emprunt(models.Model):
    media = models.ForeignKey(Media, on_delete=models.CASCADE)
    emprunteur = models.ForeignKey(Emprunteur, on_delete=models.CASCADE)
    date_emprunt = models.DateField(default=timezone.now)
    duree_jours = models.PositiveIntegerField(default=7)
    date_retour = models.DateTimeField(null=True, blank=True)

    @property
    def est_en_retard(self):
        return timezone.now().date() > self.date_emprunt + timedelta(days=self.duree_jours)

    def __str__(self):
        return f"{self.media} emprunté par {self.emprunteur}"

class PlateauJeu(models.Model):
    nom = models.CharField(max_length=100)
    description = models.TextField()
    disponible = models.BooleanField(default=True)

    def __str__(self):
        return self.nom

class EmpruntPlateauJeu(models.Model):
    emprunteur = models.ForeignKey(Emprunteur, on_delete=models.CASCADE)
    plateau = models.ForeignKey(PlateauJeu, on_delete=models.CASCADE)
    date_emprunt = models.DateTimeField(default=timezone.now)
    date_retour = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.emprunteur} a emprunté {self.plateau}"
