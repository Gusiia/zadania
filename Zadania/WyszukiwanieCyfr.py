tekst = "j012ty43a4p5q7s68"
cyfra = 0
znak = "0"
for i in range(len(tekst)):
    if "0" in tekst:
        if tekst[i].isnumeric():
            if int(tekst[i]) == cyfra:
                cyfra = cyfra + 1
    else:
        print("Brak")

print(cyfra)


