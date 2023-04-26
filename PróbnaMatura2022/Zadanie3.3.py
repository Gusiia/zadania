def czy_pierwsza(n: int):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

plik = open("liczby.txt")
suma = 0
for wiersz in plik:
    n = int(wiersz)
    for i in range(2, n):
        if i % 2 != 0:
            print(i)

print(suma)
