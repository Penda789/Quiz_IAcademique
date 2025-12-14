from django.contrib import admin
from .models import Professeur, Cours, Etudiant, Quizz

admin.site.register(Professeur)
admin.site.register(Cours)
admin.site.register(Etudiant)
admin.site.register(Quizz)

# pour que ce soit visible dans le serveur django
# Register your models here.
