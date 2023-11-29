array = [10, 22, 64, 20, 1]
total = 0

for i in range(len(array)):
    print(array[i])

for i in array:
    print(i)


for tom in array:
    total = total + tom
print(total)

total = 0

for tom in range(len(array)) :
    total = total + array[tom]
print(total)


# Exercice 2 : Somme des Éléments d'une Liste
# Créer un algorithme qui calcule la somme des éléments d'une liste.
# Exemple :
# Entrée : [1, 2, 3, 4]
# Sortie : 10