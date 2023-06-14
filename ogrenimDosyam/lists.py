ogrenciler = ["Engin", "Derin", "Salih"]
print(ogrenciler[2])

ogrenciler.append("Ceren")
ogrenciler[1] = "Musa"
ogrenciler.remove("Musa")
print(ogrenciler)


#---------------------------------------------------------------- list constructor
sehirler = list(("Ankara", "İstanbul", "İzmir"))
print(sehirler)
print(len(sehirler))

#----------------------------------------------------------------listeleri temizleme
# print(sehirler.clear())
# print(sehirler) 


print(sehirler.count("Ankara"))
print(sehirler)
sehirler2 = sehirler.copy() #listenin kopyasını alır.

sehirler.pop(1) #indexteki veriyi siler.
sehirler.insert(1, "Konya") #indexe girilen veriyi ekler.
sehirler.reverse() #listeyi tersten yazar.
print(sehirler)
print(sehirler2)

sehirler.extend(sehirler2) #iki listeyi birleştirir.
sehirler.sort() #listeyi sıralar.
print(sehirler)