l1 = int(input("Podaj licznik pierwszego ułamka: "))
m1 = int(input("Podaj mianownik pierwszego ułamka: "))
l2 = int(input("Podaj licznik drugiego ułamka: "))
m2 = int(input("Podaj mianownik drugiego ułamka: "))
licznik_wynik = l1 * l2
mianownik_wynik = m1 * m2
li1=licznik_wynik
li2=mianownik_wynik
print("Wynik wynosi: ", licznik_wynik, "/", mianownik_wynik)
while(li1 != li2):
    if li1 > li2:
        li1=li1-li2
    else:
        li2=li2-li1


print("Wynik po skróceniu wynosi: ", int(licznik_wynik/li1), "/", int(mianownik_wynik/li2))