print("TP1 - Compteur de Mots\n")

chaine = str(input("Entrer la chaîne de caractères dont vous voulez compter les mots:\n"))
chaine = chaine.strip()
nextChar = False
mots = 1

if len(chaine) == 0:
    mots = mots - 1

for car in chaine:
    if car.isspace():
        if nextChar:
            mots = mots + 1
            nextChar = False
    else:
        nextChar = True

print("\nIl y a", mots,"mot(s) dans cette chaîne de caractères")