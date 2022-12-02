# https://adventofcode.com/2022/day/1
lista = []
calories = 0
result = []
top3 = 0
# Open file
with open("data/Input_01.txt", "r") as file:
    # read file line by line, strip from and output the lines
    for line in file:
        line = line.strip()
        lista.append(line)
    lista.append('')

# print(lista)
for number in lista:
    if number != '':
        number1 = int(number)
        calories += number1
    else:
        result.append(calories)
        calories = 0
print("Max calories: " + str(max(result)))

result.sort()
top3 = sum(result[-3:])  # sum degli ultimi 3 valori di result
print("Top 3 calories: " + str(top3))
