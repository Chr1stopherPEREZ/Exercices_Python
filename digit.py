# Importation du package random
import random

# Le programme génére un chiffre aléatoire entre 0 et 9
digit_choice = random.randint(0, 9)
result = 0

# L'utilisateur à trois tentatives
for i in range(3):
    digit_propose = int(input("Saisir un chiffre : "))

    # Vérifier si le chiffre proposé est correct
    if digit_propose == digit_choice:
        result = 1
        # Sortir de la boucle si le chiffre est correct
        break

    # Informer l'utilisateur si le chiffre proposé est correct ou non
    elif digit_propose > digit_choice:
        print("Le chiffre que vous avez proposé est supérieur à celui que j'ai choisi.")
    elif digit_propose < digit_choice:
        print("Le chiffre que vous avez proposé est inférieur à celui que j'ai choisi.")

# Vérifier si l'utilisateur a trouvé le bon chiffre
if result == 1:
    print(f"Félicitations, vous avez trouvé le bon numéro {digit_choice} !")
else:
    print(f"Vous avez perdu, le bon numéro était {digit_choice}")

# Digit.py
