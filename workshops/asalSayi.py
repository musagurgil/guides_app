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

#README

### Asal Sayı Kontrolü
# Bu, kullanıcıdan alınan bir sayının asal olup olmadığını kontrol eden basit bir Python programıdır. Program, girilen sayının asal olup olmadığını belirler ve sonucu ekrana yazdırır.

### Nasıl Çalışır
# 1. Program çalıştırıldığında, kullanıcıdan bir sayı girmesi istenir.
# 2. Girilen sayının asal olup olmadığı kontrol edilir.
# 3. Eğer girilen sayı 2'den küçükse veya negatifse, asal değildir.
# 4. Girilen sayı 2'ye eşit veya daha büyükse, sayıyı 2 ile sayının karekökü arasındaki tüm pozitif tamsayılara bölerek asal olup olmadığı kontrol edilir.
# 5. Eğer sayı herhangi bir bölen ile tam bölünürse, asal değildir. Aksi halde asaldır.
# 6. Sonuç ekrana yazdırılır.

### Kullanım
# 1. Programı çalıştırın.
# 2. İstenilen sayıyı girin.
# 3. Program, sayının asal olup olmadığını ekrana yazdıracaktır.

### Kaynaklar
# Bu program, Python programlama dilinin temel akış kontrol yapıları olan koşullu ifadeleri ve döngüleri kullanarak geliştirilmiştir.

#Musa Gürgil 15.06.2023