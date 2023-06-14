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
