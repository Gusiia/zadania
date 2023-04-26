def silnia(n):
    if n == 0:
        return 1
    else:
        return n * silnia(n - 1)

def suma(n):
    if n == 0:
        return 0
    else:
        return n + suma(n - 1)

argument = int(input("Podaj argument: "))

print(silnia(argument))

print(suma(argument))
