plik = open("mecz.txt")
suma = 0
for wiersz in plik:
    linia = wiersz.split()
for i in range(len(wiersz)-1):
    if wiersz[i] != wiersz[i+1] :
        suma = suma + 1
print(suma)

