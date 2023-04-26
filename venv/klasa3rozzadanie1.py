def policz_jedynki(ciag):
    dl = len(ciag)
    suma = 0
    for i in range(dl):
        if ciag[i] == "1":
           suma = suma + 1
    return suma

def zamien_zera_na_jedynki(ciag_zer_i_jedynek):
    ciag_po_zamianie = ""
    dlugosc = len(ciag_zer_i_jedynek)
    for i in range(dlugosc):
        if ciag_zer_i_jedynek[i] == "1":
            ciag_po_zamianie = ciag_po_zamianie + "0"
        else: ciag_po_zamianie = ciag_po_zamianie + "1"

    return ciag_po_zamianie

def zamien_binarna_na_dziesietna(ciag_zer_i_jedynek):
    dziesietna = 0
    dlu = len(ciag_zer_i_jedynek)
    for i in range(dlu):
        if ciag_zer_i_jedynek[i] == "1":
            dziesietna = dziesietna + (int(ciag_zer_i_jedynek[i]) * 2) ** ((dlu) - i-1)

        else:
            continue


    return dziesietna

ciag_zer_i_jedynek = input("Podaj liczbę binarną: ")
print("Dziesiętna wynosi:", zamien_binarna_na_dziesietna(ciag_zer_i_jedynek))
print("Po zamianie: ", zamien_zera_na_jedynki(ciag_zer_i_jedynek))
print("Ilość jedynek: ",policz_jedynki(ciag_zer_i_jedynek))




#def funkcja (a,b,x,y):
#     y = a * x + b
#def czy_na_prostej (linia1, punkt1):
min(x1,x2) <= xp <= max(x1, x2)
for i in(A):
    A[0][0] + 1
    if A[0][0] > 2:
        A[0][0] = 0
    A[1][1] + 1
    if A[1][1] > 2:
        A[1][1] = 0
    A[2][2] + 1
    if A[2][2] > 2:
        A[2][2] = 0