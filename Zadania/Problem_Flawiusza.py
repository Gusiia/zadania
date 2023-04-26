n = 7
k = 3
#lista = [x for in range(n+1)]

lista = list(range(1, n + 1))
i = 0
lista2 = []

while len(lista) != 1:
    i = (i + k - 1) % len(lista)
    lista2.append(lista.pop(i))

print(lista2)
print(lista)






