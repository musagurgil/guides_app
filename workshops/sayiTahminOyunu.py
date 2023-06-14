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

#README

### Sayı Tahmin Oyunu
# Bu Python programı, kullanıcının belirli bir aralıkta rastgele seçilen bir sayıyı tahmin etmesini sağlayan bir oyundur.

### Kullanım
# 1. Programı çalıştırın.
# 2. Program, 1 ile 10 arasında (ayarlanabilir) bir sayıyı rastgele olarak seçer.
# 3. Kullanıcıdan tahminler istenir.
# 4. Kullanıcının tahmini, seçilen sayı ile karşılaştırılır.
# 5. Doğru tahmin edilene kadar kullanıcıdan tahmin yapması istenir.
# 6. Kullanıcı doğru tahmin ettiğinde tebrik edilir, aksi halde doğru sayı gösterilir.
# 7. Oyun sona erer.

### Sınırlamalar
# - Tahmin limiti, `tahmin_limiti` değişkeni üzerinden ayarlanabilir.
# - Sayı aralığı, `baslangic` ve `bitis` değişkenleri üzerinden ayarlanabilir.

### Kaynaklar
# Bu program, Python'ın random modülünü kullanarak sayı tahmin oyununu gerçekleştirmektedir.

#Musa Gürgil