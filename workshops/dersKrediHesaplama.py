def not_hesapla():
    dersler = []
    krediler = []
    notlar = []

    ders_sayisi = int(input("Ders sayısını girin: "))

    for i in range(ders_sayisi):
        ders_adi = input("{}. dersin adını girin: ".format(i+1))
        kredi = int(input("{}. dersin kredisini girin: ".format(i+1)))
        not_ortalamasi = float(input("{}. dersin not ortalamasını girin: ".format(i+1)))

        dersler.append(ders_adi)
        krediler.append(kredi)
        notlar.append(not_ortalamasi)

    toplam_kredi = sum(krediler)
    toplam_kredi_not = 0

    for i in range(ders_sayisi):
        toplam_kredi_not += krediler[i] * notlar[i]

    genel_not_ortalamasi = toplam_kredi_not / toplam_kredi

    print("Genel Not Ortalaması: {:.2f}".format(genel_not_ortalamasi))


not_hesapla()

#README

### Not Hesaplama
# Bu, kullanıcının girdiği derslerin kredilerini ve not ortalamalarını kullanarak genel not ortalamasını hesaplayan bir Python programıdır.

### Nasıl Çalışır
# 1. Program başlatıldığında, kullanıcıdan ders sayısını girmesi istenir.
# 2. Ardından, her bir ders için ders adı, kredi ve not ortalaması bilgileri istenir.
# 3. Girilen bilgiler dersler, krediler ve notlar listelerine kaydedilir.
# 4. Toplam kredi miktarı hesaplanır ve toplam kredi ile ders kredileri ve not ortalamaları kullanılarak genel not ortalaması hesaplanır.
# 5. Sonuç, genel not ortalaması olarak ekrana yazdırılır.

### Kullanım
# 1. Programı çalıştırın.
# 2. İstenilen ders sayısını girin.
# 3. Her ders için ders adını, krediyi ve not ortalamasını girin.
# 4. Program, genel not ortalamasını ekrana yazdıracaktır.

### Kaynaklar
# Bu program, Python programlama dilinin temel veri yapıları ve döngüleri kullanılarak geliştirilmiştir.

#Musa Gürgil 15.06.2023
