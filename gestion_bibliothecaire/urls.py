from django.urls import path, include
from . import views
from django.contrib import admin


urlpatterns = [

    path('', views.home, name='home'),
    path('emprunteurs/', views.liste_emprunteurs, name='emprunteurs'),
    path('emprunteurs/', views.liste_emprunteurs, name='liste_emprunteurs'),
    path('emprunteurs/ajouter/', views.ajouter_emprunteur, name='ajouter_emprunteur'),
    path('emprunts/', views.liste_emprunts, name='liste_emprunts'),
    path('medias/supprimer/<int:media_id>/', views.supprimer_media, name='supprimer_media'),
    path('media/<int:media_id>/supprimer/', views.supprimer_media, name='supprimer_media'),
    path('medias/', views.liste_medias, name='liste_medias'),
    path('medias/supprimer/<int:media_id>/', views.supprimer_media, name='supprimer_media'),
    path('membres/', views.liste_emprunteurs, name='liste_emprunteurs'),
    path('emprunteurs/supprimer/<int:emprunteur_id>/', views.supprimer_emprunteur, name='supprimer_emprunteur'),
    path('emprunts/', views.liste_emprunts, name='liste_emprunts'),
    path('connexion/', views.page_connexion, name='connexion'),
    path('medias-disponibles/', views.medias_disponibles, name='medias_disponibles'),
    path('plateaux/', views.liste_plateaux, name='liste_plateaux'),
    path('retourner-jeu/<int:emprunt_id>/', views.retourner_emprunt_plateau, name='retourner_emprunt_plateau'),
    path('supprimer-jeu/<int:emprunt_id>/', views.supprimer_emprunt_plateau, name='supprimer_emprunt_plateau'),
    path('livres/', views.liste_livres, name='liste_livres'),
    path('dvds/', views.liste_dvds, name='liste_dvds'),
    path('cds/', views.liste_cds, name='liste_cds'),
    path('bibliothecaire/', views.medias_disponibles, name='bibliothecaire'),
    path('membre/modifier/<int:emprunteur_id>/', views.modifier_emprunteur, name='modifier_emprunteur'),


]