monety = [5,2,1,0.5,0.2,0.1]
ilosc_monet = [2,1,3,1,1,4]
reszta = float(input("Podaj resztę do wydania "))
suma_monet = 0
lista = []
for i, moneta in enumerate(monety):
    while reszta >= moneta and ilosc_monet[i] > 0:
        reszta = reszta - moneta
        ilosc_monet[i] = ilosc_monet[i] - 1
        suma_monet = suma_monet + moneta
        lista.append(moneta)

if suma_monet < reszta:
    print("Nie ma monet")
else:
    print(lista)












