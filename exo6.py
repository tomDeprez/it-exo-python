# Exercice 6 : Compteur de Mots
# Écrire un script qui compte le nombre de mots dans une phrase.
# Exemple :
# Entrée : "Le test logiciel est essentiel"
# Sortie : 5

prompt = " Le test logiciel est essentiel"

array = []
space = False
var = ""
for i in prompt:
    if i == " ":
        if var != "" :
            array.append(var)
        var = ""
    else :
        var = var + i

if i != " ":
    array.append(var)


result = 0
for i in array :
    result = result + 1

print(result)