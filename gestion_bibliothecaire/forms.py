from django import forms
from .models import Emprunteur, Emprunt

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