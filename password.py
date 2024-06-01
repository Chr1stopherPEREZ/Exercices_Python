# Importation du package random
import random

# Demander à l'utilisateur de saisir la longueur du mot de passe
passwordcreate = int(input("Donner la longueur du mot de passe "))

# Liste des caractères utilisables
s = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!#$%&()*+,-./:;<=>?@[]^_`{|}~"

# Regrouper les caractères séléctionnées aléatoirement en un seul mot
password = "".join(random.sample(s, passwordcreate))

# Afficher le mot de passe généré
print(password)

# Password.py
