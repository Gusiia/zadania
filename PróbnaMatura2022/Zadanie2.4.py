def rysuj(liczba: int, wynik:int):
    N = 100000
    if 2 * liczba <= N or 2 * liczba <= wynik:
        lista.append(2 * liczba)
        rysuj(2 * liczba, wynik)
    if 2 * liczba + 1 <= N or 2 * liczba + 1 <= wynik:
        lista.append(2 * liczba +1)
        rysuj(2 * liczba + 1, wynik)

plik = open("pary.txt")
for wiersz in plik:
    liczby = wiersz.split()
    liczba_x = int(liczby[0])
    liczba_y = int(liczby[1])
    lista = []


    rysuj(liczba_x, liczba_y)
    if liczba_y in lista:
        print(liczba_x, ":", liczba_y)






