
def czy_pierwsza(n):

    for i in range(2, n):
        if n % i == 0:
            return False
    return True

plik = open("liczby.txt")
liczba_pierwszych = 0
for wiersz in plik:
    n = int(wiersz)
    if czy_pierwsza(n-1):
        liczba_pierwszych = liczba_pierwszych + 1
print("Liczba pierwszych: ", liczba_pierwszych)