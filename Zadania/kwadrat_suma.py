plik = open("kwadrat_do_suma.txt")
lista = []

for wiersz in plik:
    dane = wiersz.split()
    dane_int = list(map(lambda x: int(x), dane))
    lista.append(dane_int)

suma = lista[0][0]
suma = suma + int(lista[4][4])
x, y = 0, 0

while x < 4 and y < 4:
    if lista[y+1][x] > lista[y][x+1]:
        y += 1
    else:
        x += 1
    suma += lista[y][x]

print(suma)