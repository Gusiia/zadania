m = [[0, 0], [1, 1], [2, 2]]
n = len(m)
A = [[3, 2, 4], [5, 1, 3], [1, 6, 2]]

for i in range(n):
    j = i
    print("i = ", i, "j = ", j)
print("---")
for i in range(n):
    j = i
    i = (i + 1) % 3
    print("i = ", i, "j = ", j)
print("---")
for i in range(n):
    j = i
    i = (i + 2) % 3
    print("i = ", i, "j = ", j)
print("---")
for i in range(n):
    j = 2 - i
    print("i = ", i, "j = ", j)
print("---")
for i in range(n):
    j = 2 - i
    i = (i + 1) % 3
    print("i = ", i, "j = ", j)
print("---")
for i in range(n):
    j = 2 - i
    i = (i + 2) % 3
    print("i = ", i, "j = ", j)

#00 11 22 \
#10 21 02 \
#20 01 12 \
#02 11 20 /
#12 21 00 /
#22 01 10 /



detABC = A[0][0] * A[1][1] * A[2][2] + A[1][0] * A[2][1] * A[0][2] + A[2][0] * A[0][1] * A[1][2] - A[0][2] * A[1][1] * A[2][0] - A[1][2] * A[2][1] * A[0][0] - A[2][2] * A[0][1] * A[1][0]

print("Macierz wynosi: ", detABC)