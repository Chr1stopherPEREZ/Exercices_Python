# Demander à l'utilisateur de saisir une chaîne de caractères
text = str(input("Donner une chaîne de caractère: "))


# Fonction pour générer un acronyme à partir d'une chaîne de caractères
def acronym_gen(chaine):
    # Séparer la chaîne en mots individuels
    words = chaine.split()

    # Initialiser une chaîne vide pour l'acronyme
    acronym = ""

    # Parcourir chaque mot dans la liste des mots
    for i in words:
        # Ajouter la première lettre de chaque mot en majuscule à l'acronyme
        acronym = acronym + str(i[0]).upper()

    # Retourner l'acronyme et la liste des mots
    return acronym, words


# Appeler la fonction acronym_gen et stocker les résultats dans 'acronym' et 'words'
acronym, words = acronym_gen(text)

# Afficher le texte original fourni par l'utilisateur
print(f"Voici votre texte: {text}")

# Afficher la liste des mots du texte
print(f"Voici les mots du texte: {words}")

# Afficher l'acronyme généré
print(f"Voici votre Acronyme: {acronym}")

# Acronym.py
