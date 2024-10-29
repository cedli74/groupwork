# Fonction pour vérifier si un nombre est premier
def est_premier(n):
    """
    Vérifie si un nombre est un nombre premier.

    Un nombre premier est un nombre entier supérieur à 1 qui n'est divisible que par 1 et lui-même.

    Paramètres:
    n (int): Le nombre à vérifier.

    Retourne:
    bool: True si le nombre est premier, False sinon.
    """
    # Les nombres inférieurs ou égaux à 1 ne sont pas premiers
    if n <= 1:
        return False
    # On vérifie si n est divisible par un nombre de 2 à la racine carrée de n
    for i in range(2, int(n**0.5) + 1):
        # Si n est divisible par i, alors ce n'est pas un nombre premier
        if n % i == 0:
            return False
    # Si n n'est divisible par aucun nombre dans la boucle, c'est un nombre premier
    return True

# Fonction pour générer la liste de tous les nombres premiers jusqu'à une certaine limite
def liste_nombres_premiers(limite):
    """
    Génère une liste de nombres premiers jusqu'à une limite donnée.

    Paramètres:
    limite (int): La limite jusqu'à laquelle rechercher les nombres premiers.

    Retourne:
    list: Une liste contenant tous les nombres premiers jusqu'à la limite spécifiée.
    """
    # Liste pour stocker les nombres premiers
    nombres_premiers = []
    # Parcours de tous les nombres de 2 jusqu'à la limite donnée
    for num in range(2, limite + 1):
        # On vérifie si le nombre actuel est premier
        if est_premier(num):
            # Si oui, on l'ajoute à la liste
            nombres_premiers.append(num)
    # On retourne la liste complète des nombres premiers
    return nombres_premiers

# Exemple d'utilisation du code
limite = 100  # Limite jusqu'à laquelle on souhaite lister les nombres premiers
print(f"Les nombres premiers jusqu'à {limite} sont : {liste_nombres_premiers(limite)}")

