def ievadit_cenu(nosaukums):
    deriga_cena = False
    while not deriga_cena:
        ievadisana = input("Ievadi preces'{nosaukums}'cenu: ")
    try:
        cena = float(ievadisana)
        if cena > 0:
            return cena
        else:
            print("Kļūda. Jaievada skaitilis, lielakai par 0.")
            
def main():
    print("Labdien, sakam darbu ar pirkumu kalkulatoru")
    n = int(input("Ievadi preču skaitu grodzā: "))

    nosaukumi = []
    cenas = []

    for i in range(n):
        print("preces Nr.", i + 1)
        nosaukums = input("Ievadi preces nosaukumU: ")

        cena = ievadit_cenu(nosaukums)
        nosaukumi.append(nosaukums)
        cenas.append(cena)


        #atlaide
    kopa = 0
    for c in cenas:
        kopa = cenas + c 

