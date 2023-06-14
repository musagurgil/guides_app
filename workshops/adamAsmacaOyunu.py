import random

def adam_asmaca():
    kelime_listesi = ["python", "programlama", "bilgisayar", "kodlama", "algoritma"]
    kelime = random.choice(kelime_listesi)
    tahmin_edilen = "_" * len(kelime)
    harfler = []

    hak = 6

    print("Adam Asmaca Oyununa Hoş Geldiniz!")
    print("Tahmin etmeniz gereken kelime: ", tahmin_edilen)

    while hak > 0:
        harf = input("Bir harf tahmin edin: ").lower()

        if len(harf) != 1:
            print("Yalnızca bir harf girmelisiniz!")
            continue

        if harf in harfler:
            print("Bu harfi zaten tahmin ettiniz!")
            continue

        harfler.append(harf)

        if harf in kelime:
            yeni_tahmin = ""
            for i in range(len(kelime)):
                if harf == kelime[i]:
                    yeni_tahmin += harf
                else:
                    yeni_tahmin += tahmin_edilen[i]
            tahmin_edilen = yeni_tahmin

            print("Tebrikler! Doğru tahmin:", tahmin_edilen)

            if "_" not in tahmin_edilen:
                print("Tebrikler! Kelimeyi doğru tahmin ettiniz.")
                break
        else:
            hak -= 1
            print("Yanlış tahmin! Kalan hak:", hak)

    if hak == 0:
        print("Üzgünüm, hakkınız bitti. Doğru kelime:", kelime)

    print("Oyun sona erdi.")

adam_asmaca()

