import math

def toplama(sayilar):
    return sum(sayilar)

def cikarma(sayi1, sayi2):
    return sayi1 - sayi2

def carpma(sayilar):
    carpim = 1
    for sayi in sayilar:
        carpim *= sayi
    return carpim

def bolme(sayi1, sayi2):
    if sayi2 != 0:
        return sayi1 / sayi2
    else:
        print("Hata: Sıfıra bölme hatası!")
        return None

def kare(sayi):
    return sayi ** 2

def kok(sayi):
    return math.sqrt(sayi)

def faktoriyel(sayi):
    if sayi < 0:
        print("Hata: Negatif sayının faktöriyeli hesaplanamaz!")
        return None
    else:
        return math.factorial(sayi)

def hesap_makinesi():
    print("Hesap Makinesi")
    while True:
        print("İşlem Seçin:")
        print("1. Toplama")
        print("2. Çıkarma")
        print("3. Çarpma")
        print("4. Bölme")
        print("5. Kare")
        print("6. Karekök")
        print("7. Faktöriyel")
        print("8. Çıkış")
        secim = input("Seçiminizi yapın (1-8): ")

        if secim == '8':
            print("Hesap makinesi kapatılıyor...")
            break

        if secim not in ['1', '2', '3', '4', '5', '6', '7']:
            print("Geçersiz seçim! Lütfen tekrar deneyin.")
            continue

        if secim in ['1', '3']:
            sayi_adedi = int(input("Kaç sayıyla işlem yapmak istiyorsunuz? "))
            sayilar = []
            for i in range(sayi_adedi):
                sayi = float(input(f"{i+1}. sayıyı girin: "))
                sayilar.append(sayi)
        
        if secim == '1':
            sonuc = toplama(sayilar)
        elif secim == '2':
            sayi1 = float(input("Birinci sayıyı girin: "))
            sayi2 = float(input("İkinci sayıyı girin: "))
            sonuc = cikarma(sayi1, sayi2)
        elif secim == '3':
            sonuc = carpma(sayilar)
        elif secim == '4':
            sayi1 = float(input("Bölünen sayıyı girin: "))
            sayi2 = float(input("Bölen sayıyı girin: "))
            sonuc = bolme(sayi1, sayi2)
        elif secim == '5':
            sayi = float(input("Bir sayı girin: "))
            sonuc = kare(sayi)
        elif secim == '6':
            sayi = float(input("Bir sayı girin: "))
            sonuc = kok(sayi)
        elif secim == '7':
            sayi = int(input("Bir sayı girin: "))
            sonuc = faktoriyel(sayi)
            if sonuc is None:
                continue

        print("Sonuç: ", sonuc)

hesap_makinesi()

#README

### Hesap Makinesi
# Bu Python programı, kullanıcının basit matematiksel işlemler yapmasını sağlayan bir hesap makinesi uygulamasıdır.

### İşlemler
# Hesap makinesi aşağıdaki işlemleri destekler:
# - Toplama
# - Çıkarma
# - Çarpma
# - Bölme
# - Kare alma
# - Karekök alma
# - Faktöriyel hesaplama

### Kullanım
# 1. Programı çalıştırın.
# 2. İstenilen işlemi seçin.
# 3. İşleme göre gerekli sayıları girin.
# 4. Sonuç ekrana yazdırılır.
# 5. İşlem seçme menüsüne dönerek başka bir işlem seçebilirsiniz.
# 6. Çıkış seçeneği ile programı sonlandırabilirsiniz.

### Sınırlamalar
# - Bölme işlemi sırasında sıfıra bölme hatası kontrol edilir ve hata mesajı verilir.
# - Negatif sayıların faktöriyeli hesaplanamaz ve hata mesajı verilir.

### Örnek
# Örnek giriş ve çıkış:
# Hesap Makinesi
# İşlem Seçin:
# Toplama
# Çıkarma
# Çarpma
# Bölme
# Kare
# Karekök
# Faktöriyel
# Çıkış
# Seçiminizi yapın (1-8): 1
# Kaç sayıyla işlem yapmak istiyorsunuz? 3
# sayıyı girin: 5
# sayıyı girin: 7
# sayıyı girin: 3
# Sonuç: 15.0
# Bu örnekte, kullanıcı tarafından seçilen işlem toplama (1) olarak belirlenmiştir. Ardından, 5, 7 ve 3 sayıları girilerek toplama işlemi yapılmış ve sonuç 15.0 olarak elde edilmiştir.

### Kaynaklar
# Bu program, Python dilinde döngülerin, koşullu ifadelerin ve matematik modülünün kullanımını içermektedir.

#Musa Gürgil 15.06.2023
