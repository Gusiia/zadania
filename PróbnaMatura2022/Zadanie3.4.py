plik = open("liczby.txt")
lista = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

for wiersz in plik:
#    print(wiersz)
    h = hex(int(wiersz))
#    print(h)
    wyraz = h[2:]
    print(wyraz)
    for i in range(len(wyraz)):
        if wyraz[i] == 1:
            lista = lista[2] + 1

print(lista)

