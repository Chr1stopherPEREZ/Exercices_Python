# Importation du package random
import random

# Liste des choix possibles
choice = ["Pierre", "Papier", "Ciseaux", "Puit"]

#  Scores
score_RPSW = 0
score_player = 0

# Boucle infinie pour permettre plusieurs tours de jeu jusqu'à ce que l'utilisateur décide de quitter
while True:

    # Sélection aléatoire d'un choix pour l'ordinateur
    RPSW = random.choice(choice)

    # Demander à l'utilisateur de saisir son choix
    player = str(
        input("Pierre, Papier, Ciseaux ou Puit ? Pour quitter, tapez Fin: ")
    ).capitalize()

    # Condition pour quitter le jeu
    if player == "Fin":
        print("Merci d'avoir joué !")
        print(f"Score du programme: {score_RPSW}")
        print(f"Score du joueur: {score_player}")
        break

    # Vérifier si le choix de l'utilisateur est valide
    if player not in choice:
        print("Merci d'utiliser Pierre, Papier, Ciseaux ou Puit.")
    else:
        # Afficher le choix du programme
        print(f"Le programme a choisi : {RPSW}")

        # Vérifier si c'est une égalité
        if player == RPSW:
            print("Égalité !")

        # Vérifier les différentes conditions de victoire ou de défaite
        elif player == "Pierre":
            if RPSW == "Papier":
                print("Perdu, le papier couvre la pierre !")
                score_RPSW += 1
            elif RPSW == "Ciseaux":
                print("Gagné, la pierre casse les ciseaux !")
                score_player += 1
            elif RPSW == "Puit":
                print("Perdu, la pierre tombe au fond du puit !")
                score_RPSW += 1

        elif player == "Papier":
            if RPSW == "Ciseaux":
                print("Perdu, les ciseaux coupent le papier !")
                score_RPSW += 1
            elif RPSW == "Pierre":
                print("Gagné, le papier couvre la pierre !")
                score_player += 1
            elif RPSW == "Puit":
                print("Gagné, le papier couvre le puit !")
                score_player += 1

        elif player == "Ciseaux":
            if RPSW == "Pierre":
                print("Perdu, la pierre casse les ciseaux !")
                score_RPSW += 1
            elif RPSW == "Papier":
                print("Gagné, les ciseaux coupent le papier !")
                score_player += 1
            elif RPSW == "Puit":
                print("Perdu, les ciseaux tombent au fond du puit !")
                score_RPSW += 1

        elif player == "Puit":
            if RPSW == "Pierre":
                print("Gagné, la pierre tombe au fond du puit !")
                score_player += 1
            elif RPSW == "Papier":
                print("Perdu, le papier couvre le puit !")
                score_RPSW += 1
            elif RPSW == "Ciseaux":
                print("Gagné, les ciseaux tombent au fond du puit !")
                score_player += 1

# RPSW.py
