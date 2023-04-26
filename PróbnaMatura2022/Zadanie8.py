liczba_c = (input("Podaj liczbę w systemie czwórkowym: "))
liczba_d = 0
dl = len(liczba_c)
for i in range(dl):
    liczba_d = liczba_d + (int(liczba_c[i])) * 4 ** (dl - i - 1)
print(liczba_d)






