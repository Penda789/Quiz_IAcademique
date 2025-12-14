from rest_framework import routers
from .views import index, Cours_ViewSest, Professeur_ViewSest, Etudiant_ViewSest, Quizz_ViewSest

# pour que nos donnes puissent etre "joignable", où on peut le voir
route= routers.DefaultRouter()
route.register('Professeur',Professeur_ViewSest)#enrengistrer les diffs route
route.register('Etudiant',Etudiant_ViewSest)
route.register('Cours',Cours_ViewSest)
route.register('Quizz',Quizz_ViewSest)
