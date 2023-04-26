class Proba:
    def __init__(self, klasa: str, poczatek: int, trwanie: int):
        self.klasa = klasa
        self.poczatek = poczatek
        self.trwanie = trwanie
        self.koniec = poczatek * 60 + trwanie

def wyswietl(lista: []):
    for i in lista:
        print(i.klasa, i.poczatek, i.trwanie, i.koniec)


plik = open("klasy.txt")
lista = []
for wiersz in plik:

    dane = wiersz.split()
    proba = Proba(str(dane[0]), int(dane[1]), int(dane[2]))
    lista.append(proba)


lista.sort(key=lambda proba: proba.koniec)

wyswietl(lista)
lista_koncowa = []

def spr(lista: []):
    for i, e in enumerate(lista):
        if int(i.koniec) <= (i.poczatek(e+1) * 60):
            lista_koncowa.append(i.klasa)


(spr(lista))

print(lista_koncowa)