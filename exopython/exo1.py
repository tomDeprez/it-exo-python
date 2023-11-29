prompt = input("Prompt : ")

array = list(prompt)
count = len(array)
result = ""

for i in range(count) :
    result = result + array[count - (i + 1)]

print(result)