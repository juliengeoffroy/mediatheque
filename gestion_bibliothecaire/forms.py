from django import forms
from .models import Emprunteur, Emprunt, Media, PlateauJeu
from .models import Media, PlateauJeu

class EmprunteurForm(forms.ModelForm):
    class Meta:
        model = Emprunteur
        fields = ['nom', 'prenom', 'adresse', 'email', 'telephone']

class EmpruntForm(forms.ModelForm):
    class Meta:
         model = Emprunt
         fields = ['media', 'emprunteur', 'date_emprunt', 'duree_jours']

class ConnexionForm(forms.Form):
    username = forms.CharField(label="Nom d'utilisateur", max_length=100)
    password = forms.CharField(label="Mot de passe", widget=forms.PasswordInput)

from django import forms
from .models import Media

class MediaForm(forms.ModelForm):
    class Meta:
        model = Media
        fields = ['titre', 'type', 'auteur', 'disponible']

from django import forms
from .models import Media, PlateauJeu

class MediaForm(forms.ModelForm):
    class Meta:
        model = Media
        fields = ['titre', 'auteur', 'disponible']
        labels = {
            'titre': "Titre du média",
            'auteur': "Auteur (optionnel)",
            'disponible': "Est disponible ?"
        }

class MediaForm(forms.ModelForm):
    class Meta:
        model = Media
        fields = ['titre', 'auteur', 'disponible']
        labels = {
            'titre': "Titre du média",
            'auteur': "Auteur (optionnel)",
            'disponible': "Est disponible ?"
        }

class PlateauJeuForm(forms.ModelForm):
    class Meta:
        model = PlateauJeu
        fields = ['nom', 'description', 'disponible']
        labels = {
            'nom': "Nom du jeu",
            'description': "Description du jeu",
            'disponible': "Est disponible ?"
        }