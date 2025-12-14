from django.db import models

class Professeur(models.Model):
    nom=models.CharField(max_length=100)
    fichier=models.FileField(upload_to='public', null=True)

class Cours(models.Model):
    nom=models.CharField(max_length=100)
    contenue=models.FileField(upload_to='public', null=True)
    Professeur=models.ForeignKey(Professeur,on_delete=models.CASCADE)


class Etudiant(models.Model):
    nom=models.CharField(max_length=100)
    prenom=models.CharField(max_length=100)
    cours=models.ForeignKey(Cours, on_delete=models.CASCADE)

class Quizz(models.Model):
    titre=models.CharField(max_length=100)
    date=models.DateField()
    lien_cours=models.ForeignKey(Cours,on_delete=models.CASCADE)

# ca cree une base de données

#python manage.py makemigrations regarde les changements dans le model par rapport aux précédentes 
# et prepare des fichiers de migrations pour la prochaine migramtions
# 
#python manage.py migrate execute la migration

# Create your models here.
