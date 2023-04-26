x1 = int(input("Podaj x1: "))
y1 = int(input("Podaj y1: "))
x2 = int(input("Podaj x2: "))
y2 = int(input("Podaj y2: "))
x3 = int(input("Podaj x3: "))
y3 = int(input("Podaj y3: "))



punktA = [x1, y1, 1]
punktB = [x2, y2, 1]
punktC = [x3, y3, 1]
ABC = [punktA, punktB, punktC]

detABC = punktA[0] * punktB[1] * punktC[2] + punktB[0] * punktC[1] * punktA[2] + punktC[0] * punktA[1] * punktB[2] - punktA[2] * punktB[1] * punktC[0] - punktB[2] * punktC[1] * punktA[0] - punktC[2] * punktA[1] * punktB[0]

print("Macierz wynosi: ", detABC)

if detABC > 0:
    print("Punkt B nie leży na odcinku AC")
if detABC == 0:
    if min(x1,x3) <= x2 <= max(x1, x3):
        if min(y1,y3) <= y2 <= max(y1, y3):
            print("Punkt B leży na odcinku AC")
    else:
        print("Punkt B nie leży na odcinku AC")
if detABC < 0:
    print("Punkt B nie leży na odcinku AC")


