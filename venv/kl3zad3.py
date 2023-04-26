tekst = input("Podaj tekst: ")
wzorzec = input("Podaj wzorzec: ")
dl = len(tekst)
dlugosc = len(wzorzec)
suma = 0

if dl < dlugosc:
    print("Podaj poprawny wzorzec")

for i in range(dl):
    if tekst[i] == wzorzec[0]:
        suma = suma + 1
    else:
        continue
print(suma)

def znajdz(tekst,litera_ze_wzorca):
    dl = len(tekst)
    for i in range(dl):
        if tekst[i] == litera_ze_wzorca








