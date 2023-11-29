# Exercice 5 : Vérification de Palindrome
# Créer un programme qui vérifie si un mot est un palindrome (se lit de la même manière dans les deux sens).
# Exemple :
# Entrée : "radar"
# Sortie : True

# r != r
# a != a
def printResult(entree, result) :
    if result == entree:
        return True
    else :
        return False
entree = "bonjour"
# bonjour
# ruojnob != bonjour
array = list(entree)

count = len(array)
result = ""
for i in range(count) : 
    result = result + array[count - (i + 1)]

print(printResult(entree, result))


result = ""
for i in array:
    result = i + result

test = printResult(entree, result)

if printResult(entree, result) :
    print(printResult(entree, result))
else :
    print(not printResult(entree, result))