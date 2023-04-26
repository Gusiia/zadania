class Przedmiot:
    def __init__(self, wartosc: int, waga: int, ilosc: int):
        self.wartosc = wartosc
        self.waga = waga
        self.ilosc = ilosc
        self.stosunek = wartosc / waga

def zamiana(lista):
    lista_elementow = []
    for element in lista:
        przedmiot = Przedmiot(element[1], element[0], element[2])
        lista_elementow.append(przedmiot)
    return lista_elementow

def wyswietl(lista):
    for i in lista:
        print(i.wartosc, i.waga, i.ilosc, i.stosunek)

lista = [[3, 10, 1], [4, 11, 2], [2, 4, 3], [5, 15, 2], [2, 3, 0]]
waga = 17
lista_przedmiotow = zamiana(lista)
lista_spakowana = []

lista_przedmiotow.sort(key=lambda przedmiot: przedmiot.stosunek)
lista_przedmiotow.reverse()
#wyswietl(lista_przedmiotow)

def pakowanie(waga, lista):
    for przedmiot in lista:
        for i in range:
            lista_spakowana.append(przedmiot)
            waga -= przedmiot.stosunek[i]
            przedmiot.ilosc[i] -= 1
            if przedmiot.ilosc[i] == 0:
                lista.remove(przedmiot)
            if waga == 0:
                break
        if waga == 0:
            break
    return lista_spakowana


pakowanie(waga, lista_przedmiotow)
for przedmiot in lista_spakowana:
    print(przedmiot.waga, przedmiot.wartosc)