def todo_list():
    tasks = []

    while True:
        print("To-Do List Uygulamasına Hoş Geldiniz!")
        print("Yapmak istediğiniz işlemi seçin:")
        print("1. Görevleri Listele")
        print("2. Görev Ekle")
        print("3. Görev Tamamla")
        print("4. Çıkış")

        secim = input("Seçiminizi yapın (1-4): ")

        if secim == '1':
            if len(tasks) == 0:
                print("Listenizde herhangi bir görev bulunmamaktadır.")
            else:
                print("Görevler:")
                for i, task in enumerate(tasks, start=1):
                    print(f"{i}. {task}")

        elif secim == '2':
            yeni_gorev = input("Eklemek istediğiniz görevi girin: ")
            tasks.append(yeni_gorev)
            print(f"{yeni_gorev} görevi eklendi.")

        elif secim == '3':
            if len(tasks) == 0:
                print("Tamamlanacak görev bulunmamaktadır.")
            else:
                tamamlanan_gorev = int(input("Tamamlanan görevin numarasını girin: "))
                if tamamlanan_gorev < 1 or tamamlanan_gorev > len(tasks):
                    print("Geçersiz görev numarası!")
                else:
                    tamamlanan = tasks.pop(tamamlanan_gorev - 1)
                    print(f"{tamamlanan} görevi tamamlandı.")

        elif secim == '4':
            print("To-Do List Uygulaması kapatılıyor...")
            break

        else:
            print("Geçersiz seçim! Lütfen tekrar deneyin.")

        print()

todo_list()

#README

### To-Do List Uygulaması
# Bu Python programı, kullanıcının yapılacaklar listesi oluşturmasına ve yönetmesine olanak sağlayan basit bir To-Do List uygulamasıdır.

### Kullanım
# 1. Programı çalıştırın.
# 2. Menüden yapmak istediğiniz işlemi seçin:
#    - **1. Görevleri Listele**: Mevcut görevleri listeler.
#    - **2. Görev Ekle**: Yeni bir görev ekler.
#    - **3. Görev Tamamla**: Tamamlanan bir görevi işaretler.
#    - **4. Çıkış**: Uygulamadan çıkar.
# 3. İlgili seçeneği seçtikten sonra, gerekli girişleri yapın veya talimatları izleyin.
# 4. Program, işlemi gerçekleştirir ve sonuçları ekrana yazdırır.

### Sınırlamalar
# - Program, kullanıcının sadece menüde belirtilen seçenekleri girmesini bekler. Geçersiz seçenekler için hata mesajı verilebilir.
# - Programın mevcut sürümünde, görevler sadece metin tabanlı olarak saklanır ve her çalıştırmada sıfırlanır.

### Kaynaklar
# Bu program, Python'ın temel kontrol yapıları ve listeler gibi dil özelliklerini kullanarak bir To-Do List uygulaması oluşturur.

#Musa Gürgil 15.06.2023


