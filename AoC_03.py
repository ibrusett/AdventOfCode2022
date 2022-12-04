# https://adventofcode.com/2022/day/3
from collections import Counter

lista = []
result = []
alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

somma = 0
# Open file
with open("data/Input_03.txt", "r") as file:
    # read file line by line, strip from  and output the lines
    for line in file:
        line = line.strip()
        lista.append(line)

for riga in lista:
    meta = int(len(riga) / 2)  # calcolo la metà
    uno = riga[:meta]  # prima metà del valore
    due = riga[meta:]  # seconda meta del valore
    for a in uno:  # ciclo sulla prima meta finche trovo il valore che esiste anche nella seconda meta
        if a in due:
            value = alphabet.find(a) + 1
            result.append(a)
            somma += value
            break
print("parte 1: ", somma)

print(lista)  # calcolo quanti gruppi sono
f = 0
for i in range(len(lista) // 3):  # conto quanti gruppi da 3 ci sono
    a = Counter(lista[i * 3:i * 3 + 3][0])  # primo zaino, conto le occorrenze dei caratteri nella prima stringa
    b = Counter(lista[i * 3:i * 3 + 3][1])  # secondo zaino
    c = Counter(lista[i * 3:i * 3 + 3][2])  # terzo zaino
    d = list((a & b & c).keys())  # & fa l'and logico tra i tre dizionari ed estrae la chiave rimanente
    e = alphabet.find(d[0]) + 1
    f += e
    # d contiene la chiave del dizionario costruito con Counter che conta le occorrenze
    print(a, b, c, d, e)
print("Parte 2: ", f)


# ho copiato da qui
def dic(data):
    return sum([alphabet.index(list((Counter(data[i * 3:i * 3 + 3][0]) &
                                     Counter(data[i * 3:i * 3 + 3][1]) &
                                     Counter(data[i * 3:i * 3 + 3][2])).keys())[0]) + 1
                for i in range(len(data) // 3)])


print("Parte 2 rubata: ", dic(lista))
