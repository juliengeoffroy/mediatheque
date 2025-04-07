from django.urls import path , include
from . import views

urlpatterns = [
    path('', views.media_list, name='media_list'),
    path('', views.media_list, name='liste_medias'),
    path('membres/', views.liste_membres, name='liste_membres'),
]

