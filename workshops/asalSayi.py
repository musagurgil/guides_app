sayi = int(input("Bir sayı girin: "))
asalMi = True

if sayi < 2:
    asalMi = False
else:
    for x in range(2, int(sayi**0.5) + 1):
        if (sayi % x) == 0:
            asalMi = False
            break

if asalMi:
    print("ASAL")
else:
    print("ASAL DEĞİL")
