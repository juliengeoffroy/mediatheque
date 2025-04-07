from django.shortcuts import render
from gestion_bibliothecaire.models import Media, Emprunteur, Emprunt

def media_list(request):
   medias = Media.objects.all()
   return render(request, 'consultation_membre/media_list.html', {'medias': medias})

def liste_membres(request):
   membres = Emprunteur.objects.all()
   return render(request, 'consultation_membre/liste_membres.html', {'membres': membres})

def liste_emprunts(request):
   emprunts = Emprunt.objects.select_related('media', 'emprunteur').all()
   return render(request, 'gestion_bibliothecaire/liste_emprunts.html', {'emprunts': emprunts})


def liste_emprunts(request):
   emprunts = Emprunt.objects.all()
   emprunts_plateaux = EmpruntPlateauJeu.objects.all()
   return render(request, 'gestion_bibliothecaire/liste_emprunts.html', {
      'emprunts': emprunts,
      'emprunts_plateaux': emprunts_plateaux
   })
