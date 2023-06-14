
#s ubstring
mesaj = "Bu bir test mesajıdır."

print(mesaj[2:5])

yeniMesaj = mesaj[12:13]
print(yeniMesaj)

# len
print(len(mesaj))
yeniMesaj2 = mesaj[len(mesaj)-1:len(mesaj)]
print(yeniMesaj2)

# lower upper
print(mesaj.upper())
print(mesaj.lower())

# replace 
print(mesaj.replace("ı","i")) 
print(mesaj.replace("a","e") )

# split ve (strip(boşlukları siler)
bilgi = "Musa,Gürgil,26,Ankara".strip()
print(bilgi.split())
print("Adı = " + bilgi.split(",")[0])

#input
adi = input("Adınız ?")
soyadi = input("Soyadınız ?")
yasi=input("Yaşınız ?")
sehir=input("Şehriniz ?")
sayi1=input("Sayı 1 =?")
sayi2=input("Sayı 2 =?")
print(adi+ " " +soyadi+ " "+ sehir+ " " + yasi)
print(int(sayi1)+int(sayi2))