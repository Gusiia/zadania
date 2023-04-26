plik = open("nawiasy.txt")

for wiersz in plik:
    linia = wiersz.split()
    print(wiersz)

a = 0
b = 0
s = 1
for i in range(len(wiersz)):
    if wiersz[i] == "[":
        a = a + 1
    if wiersz[i] == "]":
        b = b + 1

    if wiersz[i] == "[":
        s = s + 1
        if wiersz[i + 1] == "[":
            s = s + 1
    if wiersz[i] == "]":
        s = s - 1




print("głębokość: ", s)
if a == b:
    print("Jest poprawny")
else:
    print("Nie jest poprawny")