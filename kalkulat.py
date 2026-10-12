def ievadit_cenu(nosaukums):
    deriga_cena = False
    while not deriga_cena:
        ievadisana = input("Ievadi preces'{nosaukums}'cenu: ")
    try:
        cena = float(ievadisana)
        if cena > 0
            return cena
        else:
            print("Kļūda. Jaievada skaitilis, nevis burts.")
