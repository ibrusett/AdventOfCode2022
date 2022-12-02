# https://adventofcode.com/2022/day/2
lista = []
result = 0
# Open file
with open("data/Input_02.txt", "r") as file:
    # read file line by line, strip from  and output the lines
    for line in file:
        line = line.strip()
        lista.append(line)
print(lista)
# A = rock - B = paper - C = scissor
# X = rock - Y = paper - Z = scissor
# 1 = rock - 2 = paper - 3 = scissor
# 0 lose - 3 draw - 6 win
dict1 = {"A": 1, "B": 2, "C": 3, "X": 1, "Y": 2, "Z": 3}
dict2 = {"A X": 3, "A Y": 6, "A Z": 0, "B X": 0, "B Y": 3, "B Z": 6, "C X": 6, "C Y": 0, "C Z": 3}
for element in lista:
    point = dict1[element[2]]
    win = dict2[element]
    result += point + win
print("Result 1: " + str(result))
# A = rock - B = paper - C = scissor
# X = lose - Y = draw - Z = win
# 1 = rock - 2 = paper - 3 = scissor
# 0 lose - 3 draw - 6 win
result = 0
dict3 = {"A X": 0+3, "A Y": 3+1, "A Z": 6+2, "B X": 0+1, "B Y": 3+2, "B Z": 6+3, "C X": 0+2, "C Y": 3+3, "C Z": 6+1}
for element in lista:
    win = dict3[element]
    result += win
print("Result 2: " + str(result))
