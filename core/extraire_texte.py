import pdfplumber

def extraction(chemin):
    with pdfplumber.open(chemin) as pdf:
        page = pdf.pages[0]           # première page seulement
        texte = page.extract_text()   # extrait le texte
    return texte 

chemin = "C:/Users/psow6/OneDrive/Bureau/COURS/L3_Cours/SAS/coursMiage2018.pdf"
print(extraction(chemin))
