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
