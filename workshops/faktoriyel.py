sayi = int(input("Sayı : "))

faktoriyel = 1

if sayi<0:
    print("Negatif sayıların faktoriyeli hesaplanamaz")
elif sayi==0:
    print("Sonuç : 1")
else:
    for i in range(1,sayi+1):
        faktoriyel = faktoriyel * i
    print("Sonuç : ",faktoriyel)

#README

### Faktöriyel Hesaplama
# Bu Python programı, kullanıcının girdiği bir sayının faktöriyelini hesaplamayı sağlar.

### Nasıl Çalışır
# Program, kullanıcıdan bir sayı girişi alır. Ardından, girilen sayının faktöriyelini hesaplar ve sonucu ekrana yazdırır.
# - `sayi`: Kullanıcıdan alınan sayı girişi.
# - `faktoriyel`: Faktöriyel değerini tutan değişken.

### Kullanım
# 1. Programı çalıştırın.
# 2. İstenilen şekilde bir sayıyı girin.
# 3. Program, girilen sayının faktöriyelini hesaplayacaktır.
# 4. Sonuç ekrana yazdırılır.

### Örnek
# Örnek giriş ve çıkış:
# Sayı: 5
# Sonuç: 120
# Bu örnekte, kullanıcı tarafından girilen 5 sayısının faktöriyeli 120'dir.

### Sınırlamalar
# - Program, negatif sayıların faktöriyelini hesaplayamaz ve bu durumda bir hata mesajı verir.

### Kaynaklar
# Bu program, Python dilinde döngülerin ve koşullu ifadelerin kullanımını içermektedir.

#Musa Gürgil 15.06.2023


