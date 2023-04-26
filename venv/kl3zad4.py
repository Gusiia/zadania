
class Point:
    x = None
    y = None
    def __init__(self, x, y):
        self.x = x
        self.y = y
#    def wyzeruj(self):
#        self.x = 0
#        self.y = 0

class Linia:
    A = None
    B = None
    C = None
    def __init__(self, A, B, C):
        self.A = A
        self.B = B
        self.C = C


def sprawdz_czy_nad (punkt:Point, prosta:Linia):
    if 0 > prosta.A * punkt.x + prosta.B * punkt.y + prosta.C:
        return True

    return False

def sprawdz_czy_na (punkt:Point, prosta:Linia):
    if 0 == prosta.A * punkt.x + prosta.B * punkt.y + prosta.C:
        return True

    return False

def sprawdz_czy_pod (punkt:Point, prosta:Linia):
    if 0 < prosta.A * punkt.x + prosta.B * punkt.y + prosta.C:
        return True

    return False

x1 = int(input("Podaj parametra x1: "))
y1 = int(input("Podaj parametra y1: "))
punkt1 = Point(x1, y1)

x2 = int(input("Podaj parametra x2: "))
y2 = int(input("Podaj parametra y2: "))
punkt2 = Point(x2, y2)


a = int(input("Podaj parametra a: "))
b = int(input("Podaj parametra b: "))
c = int(input("Podaj parametra c: "))
prosta = Linia(a, b, c)

if sprawdz_czy_na(punkt1, prosta):
    print("Punkty nie są po tej samej stronie")
else:
    if sprawdz_czy_na(punkt2, prosta):
        print("Punkty nie są po tej samej stronie")
    else:
        if sprawdz_czy_nad(punkt1, prosta):
            if sprawdz_czy_nad(punkt2, prosta):
                print("Punkty są po tej samej stronie")
            else:
                print("Punkty nie są po tej samej stronie")

        if sprawdz_czy_pod(punkt1, prosta):
            if sprawdz_czy_pod(punkt2, prosta):
                print("Punkty są po tej samej stronie")
            else:
                print("Punkty nie są po tej samej stronie")




