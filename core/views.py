from django.shortcuts import render
from .extraire_texte import extraction
from .models import Professeur, Etudiant, Quizz, Cours
from rest_framework import viewsets
from .serializers import Cours_Serializers
from .serializers import Quizz_Serializers
from .serializers import Etudiant_Serializers
from .serializers import Professeur_Serializers
import openai

openai.api_key="LA_CLE_API"


# UTILISATION DES DONNEES CONVERTIT EN JSONS ( c'est ça un endpoint)

class Cours_ViewSest(viewsets.ModelViewSet):
    queryset=Cours.objects.all() #recup tout les donnes enrengistre et qui sont  associeé a cette table
    serializer_class=Cours_Serializers

class Etudiant_ViewSest(viewsets.ModelViewSet):
    queryset=Etudiant.objects.all() #recup tout les donnes enrengistre et qui sont  associeé a cette table
    serializer_class=Etudiant_Serializers

class Quizz_ViewSest(viewsets.ModelViewSet):
    queryset=Quizz.objects.all() #recup tout les donnes enrengistre et qui sont  associeé a cette table
    serializer_class=Quizz_Serializers

class Professeur_ViewSest(viewsets.ModelViewSet):
    queryset=Professeur.objects.all() #recup tout les donnes enrengistre et qui sont  associeé a cette table
    serializer_class=Professeur_Serializers
# Create your views here.

def generer_qcm(request):
    fichier=request.FILES.get("fichier")# recup le contenue texte du fichier
    texte=extraction(fichier)

    prompt=f"""
    Génère un QCM de 10 questions basées sur le texte suivant.
        Format JSON strict :
        [
          {{
            "question": "…",
            "options": ["A", "B", "C", "D"],
            "answer": "A"
          }}
        ]
        
        Texte :
        {texte}
    """
    reponse = openai.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "user", "content": prompt}
            ]
    )

    qcm=reponse.choice[0].message.content

    return JsonResponse({"qcm": qcm})


