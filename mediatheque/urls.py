from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static
from gestion_bibliothecaire import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('connexion/', views.page_connexion, name='connexion'),
    path('logout/', LogoutView.as_view(next_page='connexion'), name='logout'),
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='accueil.html'), name='accueil'),
    path('bibliothecaire/', include('gestion_bibliothecaire.urls')),
    path('membre/', include('consultation_membre.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])