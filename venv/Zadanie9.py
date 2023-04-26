tekst = input("Podaj tekst: ")
dl = len(tekst)
tekst_org = list(tekst)
lista_tekst = list(tekst)
lista_tekst.reverse()
if tekst_org == lista_tekst:
    print("Jest palidromem")
else:
    print("Nie jest palidromem")

for i in range(0,(dl -1)):
    wycinek = tekst[0:5]
    if wycinek == wycinek[::-1]:
        print(wycinek)
for i in range(0,(dl -2)):
    wycinek = tekst[0:4]
    if wycinek == wycinek[::-1]:
        print(wycinek)
for i in range(0,(dl -3)):
    wycinek = tekst[0:3]
    if wycinek == wycinek[::-1]:
        print(wycinek)
