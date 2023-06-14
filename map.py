sayilar = [1, 2, 3, 4, 5, 6, 7, 8, 9]


sayillarKareli= list(map(lambda sayi : sayi**2,sayilar))

#---------------------------------------------------------------- İlk yöntem
# for sayi in sayilar:
#     sayillarKareli.append(sayi*sayi)

sayilarFiltreli = list(filter(lambda sayi : sayi>2,sayilar))

print(sayillarKareli)
print(sayilarFiltreli)

from functools import reduce
sayilarFaktoriyel = reduce(lambda x,y : x*y,sayilar)

print(sayilarFaktoriyel)