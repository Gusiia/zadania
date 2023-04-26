hex = ""
bin = input("Podaj liczbę binarną: ")
dl = len(bin)
lista = []
for i in range(0,dl,4):
    lista.append(bin[i:i+4])
print(lista)

def zamiana_bin_na_dec(ciag):
    dec = 0
    dl = len(ciag)
    for i in range(dl):
        if ciag[i] == "1":
            dec = dec + (1 * 2) ** (dl - i -1)
        else:
            continue
    return dec
for i in (lista):
    print(zamiana_bin_na_dec(i))

