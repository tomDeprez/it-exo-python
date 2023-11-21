#Exercice 3 : Recherche du Plus Grand Nombre
#
#Écrire un script qui trouve le plus grand nombre dans une liste.
#
#Exemple :
#
#Entrée : [3, 58, 11, 21]
#
#Sortie : 58

def lePlusGrandNombre(array) :
    sortie = 0

    for var in array :
        if var > sortie :
            sortie = var

    return sortie

array = [3, 58, 11, 21]
sortie = 0

for var in array :
    if var > sortie :
        sortie = var

print(sortie)
sortie = 0

for var in range(len(array)) :
    if array[var] > sortie :
        sortie = array[var]
print(sortie)



print(lePlusGrandNombre(array))
array = [51, 95, 75, 64, 217, 21, 2, 51]
print(lePlusGrandNombre(array))
#Afficher 58