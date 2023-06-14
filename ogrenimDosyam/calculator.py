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
