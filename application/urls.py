"""
URL configuration for application project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from core.views import index, Cours_ViewSest, Professeur_ViewSest, Etudiant_ViewSest, Quizz_ViewSest
from django.conf import settings
from django.conf.urls.static import static
from core.url_serializer import route as core_route
from rest_framework import routers

# importe dans le vrai fichier urls de django, jsp pk on pouvait pas le faire direct ici, mais en tt cas ca va nous creer une url/ un chemin d'acces 
route= routers.DefaultRouter()
route.registry.extend(core_route.registry)

urlpatterns = [
    path('',index),
    path('admin/', admin.site.urls),
    path('', include(route.urls)),
    path('api-auth/', include('rest_framework.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) #pour que les fichiers uploader puissent s'ouvrir
# http://127.0.0.1:8000/Professeur/  on met ca ici prcq sans la mention du model derrier ca provoque une erreur 404 
# http://127.0.0.1:8000/Cours/
# http://127.0.0.1:8000/Etudiant/
# http://127.0.0.1:8000/Quizz/

