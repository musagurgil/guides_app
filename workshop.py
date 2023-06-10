# # ---------------------------------------------------------------- sayiların yerini degistir #----------------------------------------------------------------

# # x = 10
# # y = 20

# # #-birinci çözüm#
# # # temp = x
# # # x = y
# # # y = temp

# # #-ikinci çözüm
# # x,y = y,x

# # print("x =" + str(x))
# # print("y =" + str(y))


# # ---------------------------------------------------------------- kac mile eder #----------------------------------------------------------------


# # kilometre = input("Yolculuğunuzun kilometre cinsinden uzunluğunu girin: ")
# # mil = int(kilometre) * 0.621371192
# # print("Mil olarak yolculuğunuz bu kadar =", mil)


# # ---------------------------------------------------------------- en buyuk sayi #----------------------------------------------------------------

# sayi1 = (int(input("1. Sayınızı giriniz: ")))
# sayi2 = (int(input("2. Sayınızı giriniz: ")))
# sayi3 = (int(input("3. Sayınızı giriniz: ")))

# if (sayi1 >= sayi2) and (sayi1 >= sayi3):
#     enBuyuk = sayi1
# elif (sayi2 >= sayi1) and (sayi2 >= sayi3):
#     enBuyuk = sayi2
# else:
#     enBuyuk = sayi3
# print("En Büyük :", enBuyuk)


# ---------------------------------------------------------------- hesap makinesi ----------------------------------------------------------------


# def toplama(sayi1, sayi2):
#     return sayi1 + sayi2


# def cikarma(sayi1, sayi2):
#     return sayi1 + sayi2


# def carpma(sayi1, sayi2):
#     return sayi1 + sayi2


# def bolme(sayi1, sayi2):
#     if sayi2 != 0:
#         return sayi1 / sayi2
#     else:
#         print("Hata: Sıfıra bölme hatası!")


# print("Hesap makinesi")

# while True:
#     print("İşlem Seçin:")
#     print("1: Toplama")
#     print("2: Çıkarma")
#     print("3: Çarpma")
#     print("4: Bölme")
#     print("5: Çıkış")
#     secim = input("Seçiminizi yapın (1/2/3/4/5)")

#     if secim == '5':
#         print("Hesap makinesi kapatılıyor...")
#         break

#     sayi1 = float(input("Birinci sayıyı girin!"))
#     sayi2 = float(input("İkinci sayıyı girin!"))
#     if secim == '1':
#         sonuc = toplama(sayi1, sayi2)
#         print("Sonuç: ", sonuc)
#     elif secim == '2':
#         sonuc = cikarma(sayi1, sayi2)
#         print("Sonuç: ", sonuc)
#     elif secim == '3':
#         sonuc = carpma(sayi1, sayi2)
#         print("Sonuç: ", sonuc)
#     elif secim == '4':
#         sonuc = bolme(sayi1, sayi2)
#         print("Sonuç: ", sonuc)
#         if sonuc is not None:
#             print("Sonuc: ", sonuc)
#     else:
#         print("Geçersiz seçim! Lütfen tekrar deneyin.")


# ---------------------------------------------------------------- kapsamlı hesap makinesi ----------------------------------------------------------------

import math


def toplama(sayi1, sayi2):
    return sayi1 + sayi2


def cikarma(sayi1, sayi2):
    return sayi1 - sayi2


def carpma(sayi1, sayi2):
    return sayi1 * sayi2


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
    elif sayi == 0:
        return 1
    else:
        faktoriyel = 1
        for i in range(1, sayi + 1):
            faktoriyel *= i
        return faktoriyel


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

        sayi = float(input("Bir sayı girin: "))

        if secim == '5':
            sonuc = kare(sayi)
        elif secim == '6':
            sonuc = kok(sayi)
        elif secim == '7':
            sonuc = faktoriyel(sayi)
            if sonuc is None:
                continue
        else:
            sayi2 = float(input("İkinci sayıyı girin: "))
            if secim == '1':
                sonuc = toplama(sayi, sayi2)
            elif secim == '2':
                sonuc = cikarma(sayi, sayi2)
            elif secim == '3':
                sonuc = carpma(sayi, sayi2)
            elif secim == '4':
                sonuc = bolme(sayi, sayi2)
                if sonuc is None:
                    continue

        print("Sonuç: ", sonuc)
        print("Bitti...")


hesap_makinesi()
