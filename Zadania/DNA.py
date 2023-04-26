dna1 = "ACTACGCATC"
dna2 = "TGATGCGTAG"

def sprawdz_DNA(dna1, dna2):
    for i in range(len(dna1)):
        if dna1[i] == "A":
            if dna2[i] != "T":
                return False
        if dna1[i] == "C":
            if dna2[i] != "G":
                return False
        if dna1[i] == "T":
            if dna2[i] != "A":
                return False
        if dna1[i] == "G":
            if dna2[i] != "C":
                return False


if sprawdz_DNA(dna1,dna2) == False:
    print("Nie")
else:
    print("Tak")

