cumle = input("Bir cümle girin: ").lower()
kelimeler = sorted(cumle.split())

print(*kelimeler, sep="\n")

#README

### Kelime Sıralama
# Bu Python programı, kullanıcının girdiği bir cümledeki kelimeleri alfabetik olarak sıralayan bir uygulamadır.

### Kullanım
# 1. Programı çalıştırın.
# 2. Bir cümle girin.
# 3. Program, cümleyi küçük harflere dönüştürerek her bir kelimeyi ayırır.
# 4. Kelimeler alfabetik sıraya göre sıralanır.
# 5. Sıralanmış kelimeler alt alta ekrana yazdırılır.

### Örnek
# Örnek giriş ve çıkış:
# Bir cümle girin: Merhaba dunyaya
# dunyaya
# Merhaba
# Bu örnekte, kullanıcı tarafından girilen cümle "Merhaba dunyaya" olmuştur. Program, bu cümleyi küçük harflere dönüştürerek kelime olarak ayırır. Ardından, kelimeler alfabetik sıraya göre sıralanır ve sıralanmış kelimeler "dunyaya" ve "Merhaba" olarak ekrana yazdırılır.

### Sınırlamalar
# - Program, sadece alfabetik karakterlerden oluşan kelimeleri sıralayabilir. Diğer karakterler (noktalama işaretleri, sayılar, vb.) görmezden gelinir.
# - Türkçe karakterler için doğru sıralama yapılmayabilir.

### Kaynaklar
# Bu program, Python dilinin string işleme yeteneklerini ve sıralama fonksiyonlarını kullanmaktadır.

#Musa Gürgil 15.06.2023
