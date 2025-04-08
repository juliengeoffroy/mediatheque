from django.shortcuts import render, get_object_or_404, redirect
from .models import Media, Emprunteur, Emprunt, EmpruntPlateauJeu, PlateauJeu
from .forms import EmprunteurForm, EmpruntForm
from .forms import ConnexionForm
from .forms import MediaForm, PlateauJeuForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.utils import timezone
from datetime import timedelta

def home(request):
        medias = Media.objects.all()
        return render(request, 'gestion_bibliothecaire/home.html', {'medias': medias})

def liste_emprunts(request):
    emprunts = Emprunt.objects.all()
    emprunts_plateaux = EmpruntPlateauJeu.objects.all()
    return render(request, 'gestion_bibliothecaire/liste_emprunts.html', {
        'emprunts': emprunts,
        'emprunts_plateaux': emprunts_plateaux
    })

def liste_emprunteurs(request):
    emprunteurs = Emprunteur.objects.all()
    return render(request, 'gestion_bibliothecaire/emprunteurs.html', {'emprunteurs': emprunteurs})

def ajouter_emprunteur(request):
    if request.method == 'POST':
       form = EmprunteurForm(request.POST)
       if form.is_valid():
            form.save()
            return redirect('emprunteurs')
    else:
        form = EmprunteurForm()
    return render(request, 'gestion_bibliothecaire/ajouter_emprunteur.html', {'form': form})

def ajouter_emprunt_complet(request):
    if request.method == 'POST':
        form = EmpruntForm(request.POST)
        if form.is_valid():
            emprunt = form.save()
            emprunt.media.disponible = False
            emprunt.media.save()
            return redirect('home')
    else:
        form = EmpruntForm()
    return render(request, 'gestion_bibliothecaire/ajouter_emprunt.html', {'form': form})

def supprimer_emprunteur(request, emprunteur_id):
    emprunteur = get_object_or_404(Emprunteur, id=emprunteur_id)
    emprunteur.delete()
    return redirect('liste_emprunteurs')

def liste_emprunts(request):
    emprunts = Emprunt.objects.all()
    return render(request, 'gestion_bibliothecaire/liste_emprunts.html', {'emprunts': emprunts})

def rendre_emprunt(request, emprunt_id):
    emprunt = get_object_or_404(Emprunt, id=emprunt_id)
    emprunt.media.disponible = True
    emprunt.media.save()
    emprunt.delete()
    return redirect('emprunts')

def page_connexion(request):
    return render(request, 'gestion_bibliothecaire/connexion.html')

def page_connexion(request):
    if request.method == "POST":
        form = ConnexionForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('liste_medias')  # ⚠️ à adapter à ton projet
            else:
                form.add_error(None, "Nom d'utilisateur ou mot de passe incorrect.")
                messages.error(request, "Identifiants incorrects.")
            return render(request, 'gestion_bibliothecaire/connexion.html')
    else:
        form = ConnexionForm()
    return render(request, 'gestion_bibliothecaire/connexion.html', {'form': form})

def liste_emprunts(request):
    emprunts = Emprunt.objects.all()
    return render(request, 'gestion_bibliothecaire/liste_emprunts.html', {'emprunts': emprunts})

def supprimer_media( request, media_id):
    media = get_object_or_404(Media, id=media_id)
    media.delete()
    return redirect('liste_medias')

def liste_medias(request):
    medias = Media.objects.all()
    return render(request, 'gestion_bibliothecaire/liste_medias.html', {'medias': medias})

def medias_disponibles(request):
    medias = Media.objects.all()
    return render(request, 'gestion_bibliothecaire/medias_disponibles.html', {'medias': medias})

def liste_plateaux(request):
    plateaux = PlateauJeu.objects.all()
    return render(request, 'gestion_bibliothecaire/liste_plateaux.html', {'plateaux': plateaux})

def retourner_emprunt_plateau(request, emprunt_id):
    emprunt = get_object_or_404(EmpruntPlateauJeu, id=emprunt_id)
    emprunt.date_retour = timezone.now()
    emprunt.plateau.disponible = True
    emprunt.plateau.save()
    emprunt.save()
    return redirect('liste_emprunts')

def liste_emprunts(request):
    emprunts = Emprunt.objects.all()
    emprunts_plateaux = EmpruntPlateauJeu.objects.all()
    return render(request, 'gestion_bibliothecaire/liste_emprunts.html', {
        'emprunts': emprunts,
        'emprunts_plateaux': emprunts_plateaux
    })

def supprimer_emprunt_plateau(request, emprunt_id):
    emprunt = get_object_or_404(EmpruntPlateauJeu, id=emprunt_id)
    emprunt.plateau.disponible = True
    emprunt.plateau.save()
    emprunt.delete()
    return redirect('liste_emprunts')

def liste_livres(request):
    livres = Media.objects.filter(type='livre')
    return render(request, 'gestion_bibliothecaire/liste_livres.html', {'medias': livres})

def liste_dvds(request):
    dvds = Media.objects.filter(type='dvd')
    return render(request, 'gestion_bibliothecaire/liste_dvds.html', {'medias': dvds})

def liste_cds(request):
    cds = Media.objects.filter(type='cd')
    return render(request, 'gestion_bibliothecaire/liste_cds.html', {'medias': cds})

def liste_medias(request):
    medias = Media.objects.all()
    return render(request, 'gestion_bibliothecaire/liste_medias.html', {'medias': medias})

def medias_disponibles(request):
    medias = Media.objects.filter(disponible=True)
    return render(request, 'gestion_bibliothecaire/medias_disponibles.html', {'medias': medias})

def modifier_emprunteur(request, emprunteur_id):
    emprunteur = get_object_or_404(Emprunteur, id=emprunteur_id)
    if request.method == 'POST':
        form = EmprunteurForm(request.POST, instance=emprunteur)
        if form.is_valid():
            form.save()
            return redirect('emprunteurs')  # ou vers la liste
    else:
        form = EmprunteurForm(instance=emprunteur)
    return render(request, 'gestion_bibliothecaire/modifier_emprunteur.html', {'form': form})

def liste_emprunteurs_empruntant(request):
    emprunteurs = Emprunteur.objects.filter(emprunt__isnull=False).distinct()
    return render(request, 'gestion_bibliothecaire/emprunteurs_emprunts.html', {'emprunteurs': emprunteurs})

def modifier_media(request, media_id):
    media = get_object_or_404(Media, id=media_id)
    if request.method == 'POST':
        form = MediaForm(request.POST, instance=media)
        if form.is_valid():
            form.save()
            return redirect('liste_emprunts')  # ou liste_livres / liste_cd / liste_dvd selon le type
    else:
        form = MediaForm(instance=media)
    return render(request, 'gestion_bibliothecaire/modifier_media.html', {'form': form, 'media': media})

def ajouter_livre(request):
    return ajouter_media_type(request, 'livre')

def ajouter_cd(request):
    return ajouter_media_type(request, 'cd')

def ajouter_dvd(request):
    return ajouter_media_type(request, 'dvd')

def ajouter_plateau(request):
    if request.method == 'POST':
        form = PlateauJeuForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('liste_emprunts')
    else:
        form = PlateauJeuForm()
    return render(request, 'gestion_bibliothecaire/ajouter_plateau.html', {'form': form})

def ajouter_media_type(request, media_type):
    if request.method == 'POST':
        form = MediaForm(request.POST)
        if form.is_valid():
            media = form.save(commit=False)
            media.type = media_type
            media.save()
            return redirect('liste_emprunts')
    else:
        form = MediaForm()
    return render(request, 'gestion_bibliothecaire/ajouter_media.html', {'form': form, 'type': media_type})

def espace_bibliothecaire(request):
    emprunts = Emprunt.objects.all()
    emprunts_plateaux = EmpruntPlateauJeu.objects.all()
    return render(request, 'gestion_bibliothecaire/liste_emprunts.html', {
        'emprunts': emprunts,
        'emprunts_plateaux': emprunts_plateaux
    })

def modifier_plateau(request, plateau_id):
    plateau = get_object_or_404(PlateauJeu, id=plateau_id)
    if request.method == 'POST':
        form = PlateauJeuForm(request.POST, instance=plateau)
        if form.is_valid():
            form.save()
            return redirect('liste_plateaux')  # ou 'espace_bibliothecaire' si tu préfères
    else:
        form = PlateauJeuForm(instance=plateau)
    return render(request, 'gestion_bibliothecaire/modifier_plateau.html', {'form': form})

