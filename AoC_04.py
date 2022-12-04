# https://adventofcode.com/2022/day/4
lista = []
ans1 = 0
ans2 = 0
# Open file
with open("data/Input_04.txt", "r") as file:
    # read file line by line, strip from  and output the lines
    for line in file:
        line = line.strip()
        lista.append(line)
print(lista)
for element in lista:
    pairs = element.split(",")
    area1 = pairs[0].partition("-")
    area2 = pairs[1].partition("-")
    # a contenuta in b se
    if ((int(area1[0]) >= int(area2[0])) and (int(area1[2]) <= int(area2[2]))) or ((int(area1[0]) <= int(area2[0])) and (int(area1[2]) >= int(area2[2]))) :
        ans1 += 1

    if ((int(area1[0]) <= int(area2[2])) and (int(area1[0]) >= int(area2[0]))) or \
            ((int(area1[2]) >= int(area2[0])) and (int(area1[0]) <= int(area2[0]))):
        ans2 += 1

print("Prima parte: ", ans1)
print("Seconda parte: ", ans2)

# si poteva fare creando dei range
irange = lambda a, b: range(a, b + 1)  # funzione monoriga definita come lambda [parametri]: funzione
ans3 = 0
for element in lista:
    x, y = element.strip().split(",")  # assegno a due variabili x e y le due parti dello split
    a = set(irange(*map(int, x.split("-"))))  # set che contiene gli elementi del primo range
    b = set(irange(*map(int, y.split("-"))))  # set che contiene gli elementi del secondo range
    # print(x, y, a, b, len(a & b))
    if (len(a & b) > 0):
        ans3 +=1
print("seconda parte coi range: ", ans3)