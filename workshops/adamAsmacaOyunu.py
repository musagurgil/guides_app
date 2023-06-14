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

#README

### Adam Asmaca Oyunu
# Bu, Python ile geliştirilmiş basit bir Adam Asmaca oyunudur. Oyunda rastgele seçilen bir kelimeyi tahmin etmeye çalışırsınız. Her yanlış tahminde, asılan bir adamın görseli oluşturulur.

### Kurulum
# Oyunu çalıştırmak için Python 3'e ve `random` modülüne ihtiyacınız vardır. İlgili bağımlılıkları kurmak için aşağıdaki komutu kullanabilirsiniz:


### Nasıl Oynanır
# 1. Oyunu başlatmak için `adam_asmaca()` fonksiyonunu çalıştırın.
# 2. Oyunda rastgele seçilen bir kelime belirlenir ve "_" karakterleriyle temsil edilir.
# 3. Sırasıyla harf tahminleri yapın. Yalnızca bir harf girebilirsiniz.
# 4. Doğru tahminlerde, kelimenin doğru yerlerinde harfler gösterilir.
# 5. Yanlış tahminlerde, hakkınız bir azalır.
# 6. Oyun devam eder ve doğru kelimeyi tahmin edene kadar veya hakkınız tükenene kadar devam eder.

### Kaynaklar
# Bu oyun, Python programlama dilinin temel özelliklerini ve döngülerini kullanarak geliştirilmiştir.

#Musa Gürgil 15.06.2023
