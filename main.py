"""
Nom: Nicolas Rodriguez
Groupe: 406
Description: Compteur de mots
"""

print("TP1 - Compteur de Mots\n")

chaine = str(input("Entrer la chaîne de caractères dont vous voulez compter les mots:\n"))
chaine = chaine.strip()
next_char = False
mots = 1

if len(chaine) == 0:
    mots -= 1

for character in chaine:

    if character.isspace():
        if next_char:
            mots += 1
            next_char = False
    else:
        next_char = True

print("\nIl y a", mots, "mot(s) dans cette chaîne de caractères")
