print("1. Matrisi girin:")
matris1 = [[int(input("Bir eleman girin: ")) for _ in range(3)] for _ in range(3)]

print("2. Matrisi girin:")
matris2 = [[int(input("Bir eleman girin: ")) for _ in range(3)] for _ in range(3)]

print("Sonuç Matrisi:")
sonuc_matrisi = [[matris1[i][j] + matris2[i][j] for j in range(3)] for i in range(3)]
for satir in sonuc_matrisi:
    print(satir)

#README

### Matris Toplama
# Bu Python programı, kullanıcının girdiği iki matrisi toplayan bir matris toplama uygulamasıdır. Matrisler 3x3 boyutunda olmalıdır.

### Kullanım
# 1. Programı çalıştırın.
# 2. İlk matris için 3x3 boyutunda elemanları girin.
# 3. İkinci matris için 3x3 boyutunda elemanları girin.
# 4. Program, girilen matrisleri toplayarak sonuç matrisini oluşturur.
# 5. Sonuç matrisi ekrana yazdırılır.

### Örnek
# Örnek giriş ve çıkış:
# Matrisi girin:
# Bir eleman girin: 1
# Bir eleman girin: 2
# Bir eleman girin: 3
# Bir eleman girin: 4
# Bir eleman girin: 5
# Bir eleman girin: 6
# Bir eleman girin: 7
# Bir eleman girin: 8
# Bir eleman girin: 9

# Matrisi girin:
# Bir eleman girin: 9
# Bir eleman girin: 8
# Bir eleman girin: 7
# Bir eleman girin: 6
# Bir eleman girin: 5
# Bir eleman girin: 4
# Bir eleman girin: 3
# Bir eleman girin: 2
# Bir eleman girin: 1

# Sonuç Matrisi:
# [10, 10, 10]
# [10, 10, 10]
# [10, 10, 10]
# Bu örnekte, kullanıcı tarafından girilen iki matris toplanır ve sonuç matrisi "Sonuç Matrisi" başlığı altında ekrana yazdırılır.

### Sınırlamalar
# - Program, kullanıcının tam olarak 3x3 boyutunda matrisler girmesini bekler. Diğer boyutlar için hata mesajı verebilir.

### Kaynaklar
# Bu program, Python'ın liste kavramını ve döngülerini kullanarak matris toplama işlemini gerçekleştirir.

#Musa Gürgil 15.06.2023
