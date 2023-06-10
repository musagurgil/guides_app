def selamVer(isim="Ziyaretçi", soyIsim="Girişi"):
    print("Merhaba " + isim + " " + soyIsim)


selamVer()
selamVer("Musa", "Gürgil")
selamVer("Ceren", "Gürgil")


def dikUcgenAlaniHesapla(a, b):
    return a*b/2


alan = dikUcgenAlaniHesapla(2, 3)
print(alan)


dikUcgenAlaniHesapla2 = lambda a, b: a*b/2


print(type(dikUcgenAlaniHesapla))
print(dikUcgenAlaniHesapla2(3, 6))
