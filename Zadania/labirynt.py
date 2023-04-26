class Stos:
    def __init__(self):
        self.items = []
    def push(self, element):
        self.items.append(element)
    def pop(self):
        if len(self.items) != 0:
            self.items.remove(self.items[-1])
    def top(self):
        if len(self.items) != 0:
            return self.items[-1]
        else:
            return None
class Punkt:
    def __init__(self, x: int, y: int, rozwidlenie: bool):
        self.x = x
        self.y = y
        self.rozwidlenie = rozwidlenie

def wczytaj():
    plik = open("labirynt.txt")
    lista = []
    for i in plik:
        i = i.strip()
        ram = []
        for x in range(len(i)):
            ram.append(i[x])
        lista.append(ram)

    for y in range(len(lista)):
        print(lista[y])


def krok(stos, labirynt):

    obecny_punkt = stos.top()

    if obecny_punkt.x == len(labirynt[0]) - 1 and obecny_punkt.y == len(labirynt) - 1:
        print(obecny_punkt.x, obecny_punkt.y)
        return True

    if obecny_punkt.x + 1 < len(labirynt[0]) and labirynt[obecny_punkt.y][obecny_punkt.x + 1] != '#':
        nowy_punkt = Punkt(obecny_punkt.x + 1, obecny_punkt.y, False)
        stos.push(nowy_punkt)
        if krok(stos, labirynt):
            return True
        else:
            stos.pop()

    if obecny_punkt.y + 1 < len(labirynt) and labirynt[obecny_punkt.y + 1][obecny_punkt.x] != '#':
        nowy_punkt = Punkt(obecny_punkt.x, obecny_punkt.y + 1, False)
        stos.push(nowy_punkt)
        if krok(stos, labirynt):
            return True
        else:
            stos.pop()

    if obecny_punkt.x - 1 >= 0 and labirynt[obecny_punkt.y][obecny_punkt.x - 1] != '#' and not obecny_punkt.rozwidlenie:
        nowy_punkt = Punkt(obecny_punkt.x - 1, obecny_punkt.y, True)
        stos.push(nowy_punkt)
        if krok(stos, labirynt):
            return True
        else:
            stos.pop()

    if obecny_punkt.y - 1 >= 0 and labirynt[obecny_punkt.y - 1][obecny_punkt.x] != '#' and not obecny_punkt.rozwidlenie:
        nowy_punkt = Punkt(obecny_punkt.x, obecny_punkt.y - 1, True)
        stos.push(nowy_punkt)
        if krok(stos, labirynt):
            return True
        else:
            stos.pop()



stos = Stos()
labirynt = wczytaj()
krok(stos, labirynt)









