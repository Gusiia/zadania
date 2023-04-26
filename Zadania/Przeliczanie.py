def zamien(liczba,system_liczby):
    przeliczona_liczba = 0
    dl = len(liczba)
    for i in range(dl):
        przeliczona_liczba = przeliczona_liczba + (int(liczba[i])) * system_liczby ** (dl - i - 1)
    return przeliczona_liczba



system_liczby = int(input("Podaj system liczby: "))
liczba = input(("Podaj liczbę: "))

print(zamien(liczba,system_liczby))
