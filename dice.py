# Importation du package random
import random

# Régle du jeu
print("1: Lancer le dé, 0: Quitter le programme")

# Boucle infini tant que l'utilisateur utilise le bon boutton
while True:

    # On demande à l'utlisateur de saisir un nombre
    x = int(input("Cliquer sur le bouton demander pour lancer le dé "))

    # Si l'utilisateur clique sur 0, on quitte le programme
    if x == 0:
        print("Bye, à la prochaine")
        break

    # Si l'utilisateur clique sur 1, on lance le dé
    elif x == 1:
        # Génère et affiche un nombre aléatoire entre 1 et 6
        print(random.randint(1, 6))

    # Si l'utilisateur clique sur un autre bouton, on affiche un message d'erreur
    else:
        print("Merci de cliquer sur le bon bouton pour lancer le dé")

# Dice.py
