def pierwsze(n):
    if n % pierwsze(n-1) == 0:
        return False
    return True




n = int(input("Podaj liczbę: "))
print(pierwsze(n))