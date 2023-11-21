# Exercice 4 : Calcul de la Factorielle
# Développer une fonction qui calcule la factorielle d'un nombre.
# Exemple :
# Entrée : 5
# Sortie : 120 (car 5! = 5 x 4 x 3 x 2 x 1)
# 5 * 4
# total * 3
# total * 2
# total * 1

entree = 5

for var in range(entree - 1):
    var = var + 1
    entree = var * entree


print(entree)