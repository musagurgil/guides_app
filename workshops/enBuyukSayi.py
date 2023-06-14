sayi1 = int(input("1. Sayı :"))
sayi2 = int(input("2. Sayı :"))
sayi3 = int(input("3. Sayı :"))

if (sayi1>=sayi2) and (sayi1>=sayi3):
    enBuyuk = sayi1
elif (sayi2>=sayi1) and (sayi2>=sayi3):
    enBuyuk = sayi2
else:
    enBuyuk = sayi3
    
print("En Büyük :",enBuyuk)

#README

### En Büyük Sayıyı Bulma
# Bu Python programı, kullanıcıdan üç adet sayı alarak bu sayılar arasındaki en büyük sayıyı bulmayı sağlar.

### Nasıl Çalışır
# Program, kullanıcıdan üç adet sayı girişi alır. Ardından, girilen sayılar arasında en büyük olanı belirler ve ekrana yazdırır.
# - `sayi1`, `sayi2` ve `sayi3`: Kullanıcıdan alınan üç adet sayı girişi.
# - `enBuyuk`: En büyük sayıyı tutan değişken.

### Kullanım
# 1. Programı çalıştırın.
# 2. İstenilen şekilde üç adet sayıyı girin.
# 3. Program, girilen sayılar arasındaki en büyük sayıyı belirleyecektir.
# 4. En büyük sayı ekrana yazdırılır.

### Örnek
# Örnek giriş ve çıkış:
# Sayı : 10
# Sayı : 25
# Sayı : 15
# En Büyük : 25
# Bu örnekte, kullanıcı tarafından girilen 10, 25 ve 15 sayıları arasında en büyük sayı 25'tir.

### Kaynaklar
# Bu program, Python dilindeki temel karar yapılarını ve karşılaştırma operatörlerini kullanarak geliştirilmiştir.

#Musa Gürgil 15.06.2023