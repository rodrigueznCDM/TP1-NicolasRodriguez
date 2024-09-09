print("TP1 - Compteur de Mots\n")

chaine = str(input("Entrer la chaîne de caractères dont vous voulez compter les mots:\n"))
chaine = chaine.strip()

mots = 1
next = 0

for car in chaine:
    if next == 1:
        if car.isspace():
            mots = mots + 1
            next = next - 1
            print("mot")
        else:
            print("pas mot")
            next = next - 1

    elif car.isalnum():
        print("mot?")
        next = next + 1


print("\nIl y a", mots,"mot(s) dans cette chaîne de caractères")