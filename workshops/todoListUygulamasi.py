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
