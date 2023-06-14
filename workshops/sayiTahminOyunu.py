import random

def sayi_tahmin_oyunu():
    tahmin_limiti = 3
    tahmin_sayisi = 0
    baslangic = 1
    bitis = 10

    sayi = random.randint(baslangic, bitis)

    print("Sayı Tahmin Oyununa Hoş Geldiniz!")
    print(f"{baslangic} ile {bitis} arasında bir sayı tuttum. Tahmin edebilir misin?")

    while tahmin_sayisi < tahmin_limiti:
        tahmin = int(input("Tahmininizi girin: "))

        tahmin_sayisi += 1

        if tahmin < sayi:
            print("Daha yüksek bir sayı girin.")
        elif tahmin > sayi:
            print("Daha düşük bir sayı girin.")
        else:
            print("Tebrikler! Doğru tahmin ettiniz.")
            break

    if tahmin != sayi:
        print(f"Maalesef, doğru sayıyı bulamadınız. Tutulan sayı: {sayi}")

    print("Oyun bitti.")

sayi_tahmin_oyunu()
