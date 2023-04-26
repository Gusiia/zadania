class Przedmiot:
    def __init__(self, wartosc: int, waga: int):
        self.wartosc = wartosc
        self.waga = waga
        self.stosunek = wartosc / waga

def zamiana(lista):
    lista_elementow = []
    for element in lista:
        przedmiot = Przedmiot(element[1], element[0])
        lista_elementow.append(przedmiot)
    return lista_elementow

def wyswietl(lista):
    for i in lista:
        print(i.wartosc, i.waga, i.stosunek)

lista = [[3, 10], [4, 11], [2, 4], [5, 15], [2, 3]]
waga = 15
lista_przedmiotow = zamiana(lista)
lista_spakowana = []

lista_przedmiotow.sort(key=lambda przedmiot: przedmiot.stosunek)
lista_przedmiotow.reverse()
#wyswietl(lista_przedmiotow)




def pakowanie(waga, lista):
    for przedmiot in lista:
        while waga >= przedmiot.stosunek:
            waga -= przedmiot.stosunek
            lista_spakowana.append(przedmiot)

pakowanie(waga, lista_przedmiotow)
for przedmiot in lista_spakowana:
    print(przedmiot.waga, przedmiot.wartosc)
