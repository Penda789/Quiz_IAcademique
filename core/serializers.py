from rest_framework import serializers
from .models import Etudiant, Professeur, Cours, Quizz

# permet de passer d'un modele d'une BD en format JSON ( prcq les api ne produisent/consomment que du JSON)
# CONVERSION EN JSON SEULEMENT
class Professeur_Serializers(serializers.ModelSerializer):
    class Meta :
        model=Professeur # comme son nom l'indique c'est le nom d'une tab de base de donnees
        fields='__all__' #l'objet à convertir en json

class Cours_Serializers(serializers.ModelSerializer):
    class Meta:
        model=Cours
        fields='__all__'

class Etudiant_Serializers(serializers.ModelSerializer):
    class Meta:
        model=Etudiant
        fields='__all__'

class Quizz_Serializers(serializers.ModelSerializer):
    class Meta:
        model=Quizz
        fields='__all__'