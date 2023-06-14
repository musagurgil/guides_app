def tersine_cevir(kelime):
    return kelime[::-1]

def kullanici_girdisi_al():
    kelime = input("Bir kelime girin: ")
    return kelime

def ana_program():
    kelime = kullanici_girdisi_al()
    ters_kelime = tersine_cevir(kelime)
    print("Kelimenin tersi: ", ters_kelime)

ana_program()

#README

### Kelimenin Tersini Bulma
# Bu Python programı, kullanıcının girdiği bir kelimenin tersini bulan basit bir uygulamadır.

### Kullanım
# 1. Programı çalıştırın.
# 2. Bir kelime girin.
# 3. Program, girilen kelimenin tersini hesaplar.
# 4. Ters kelime ekrana yazdırılır.

### Örnek
# Örnek giriş ve çıkış:
# Bir kelime girin: merhaba
# Kelimenin tersi: abahrem
# Bu örnekte, kullanıcı "merhaba" kelimesini girdiğinde program, kelimenin tersini hesaplayarak "abahrem" sonucunu verir.

### Sınırlamalar
# - Program, kullanıcının sadece bir kelime girmesini bekler. Cümle veya özel karakterler için optimize edilebilir.

### Kaynaklar
# Bu program, Python'ın dil özelliği olan dilimleme (slicing) yöntemini kullanarak kelimenin tersini bulur.

#Musa Gürgil 15.06.2023
