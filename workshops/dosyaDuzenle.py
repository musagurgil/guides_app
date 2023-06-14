def dosya_oku(dosya_adi):
    try:
        with open(dosya_adi, 'r') as dosya:
            icerik = dosya.read()
            print(icerik)
    except FileNotFoundError:
        print("Belirtilen dosya bulunamadı.")

def dosya_yaz(dosya_adi, icerik):
    with open(dosya_adi, 'w') as dosya:
        dosya.write(icerik)
    print("Dosya başarıyla yazıldı.")

def dosya_ekle(dosya_adi, icerik):
    with open(dosya_adi, 'a') as dosya:
        dosya.write(icerik)
    print("Dosyaya başarıyla eklendi.")
    
import os
def dosya_sil(dosya_adi):
    try:
        os.remove(dosya_adi)
        print("Dosya başarıyla silindi.")
    except FileNotFoundError:
        print("Belirtilen dosya bulunamadı.")

# Kullanım örneği
dosya_adi = "test.txt"
icerik = "Bu bir test dosyasıdır."

# Dosya okuma
dosya_oku(dosya_adi)

# Dosyaya yazma
dosya_yaz(dosya_adi, icerik)

# Dosyaya ekleme
dosya_ekle(dosya_adi, "Yeni satır eklendi.")

# Dosya tekrar okuma
dosya_oku(dosya_adi)

# Dosya silme
dosya_sil(dosya_adi)

#README

### Dosya İşlemleri
# Bu Python programı, dosya okuma, dosya yazma, dosyaya ekleme ve dosya silme gibi temel dosya işlemlerini gerçekleştirmek için kullanılır.

### Nasıl Çalışır
# Program, kullanıcıdan bir dosya adı ve gerekli içeriği alarak belirtilen işlemi gerçekleştirir.
# - `dosya_oku(dosya_adi)`: Belirtilen dosyayı okur ve içeriği ekrana yazdırır.
# - `dosya_yaz(dosya_adi, icerik)`: Belirtilen dosyaya verilen içeriği yazar. Dosya daha önce varsa üzerine yazar, yoksa yeni bir dosya oluşturur.
# - `dosya_ekle(dosya_adi, icerik)`: Belirtilen dosyaya verilen içeriği ekler. Dosya daha önce varsa içeriği dosyanın sonuna ekler, yoksa yeni bir dosya oluşturur ve içeriği yazar.
# - `dosya_sil(dosya_adi)`: Belirtilen dosyayı siler.

### Kullanım
# 1. Programı çalıştırın.
# 2. İstenilen işlemi seçin:
#    - Dosya okuma için: `dosya_oku(dosya_adi)`
#    - Dosya yazma için: `dosya_yaz(dosya_adi, icerik)`
#    - Dosyaya ekleme için: `dosya_ekle(dosya_adi, icerik)`
#    - Dosya silme için: `dosya_sil(dosya_adi)`
# 3. İlgili işlemi yapmak için gerekli parametreleri girin.
# 4. Program, istenen işlemi gerçekleştirecektir.

### Önemli Not
# Dosya işlemleri yaparken, işlem yapılacak dosyanın bulunduğu dizinde olduğunuzdan emin olun. Aksi takdirde, dosya bulunamama hatası alabilirsiniz.

### Kaynaklar
# Bu program, Python'in dosya işlemleri konusunda sağladığı standart işlevleri kullanarak geliştirilmiştir.

#Musa Gürgil 15.06.2023
