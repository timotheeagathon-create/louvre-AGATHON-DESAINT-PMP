import time

def titre():
    print("=" * 62)
    print("                  LE MYSTÈRE DU LOUVRE")
    print("=" * 62)
    time.sleep(1)
    print("Paris, une nuit de mars.")
    time.sleep(1)
    print("Quatre bijoux majeurs ont disparu de la Galerie d'Apollon.")
    time.sleep(1)
    print("Le musée fait appel à vous pour résoudre l'affaire.")
    print("=" * 62)
    time.sleep(1)
titre()

def main():
    nom_detective = input("Entrez votre nom de detective :")
        while nom_detective == "":
            nom_detective = input("Entrez votre nom de detective :")
