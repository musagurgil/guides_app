# cumle = input("Bir cümle girin: ")

# # Cümleyi küçük harfe çevirin
# cumle = cumle.lower()

# # Cümleyi kelimelere ayırın
# kelimeler = cumle.split()

# # Her bir kelimeyi alfabetik olarak sıralayın
# siralama = sorted(kelimeler)

# # Sıralanmış kelimeleri alt alta yazdırın
# for kelime in siralama:
#     print(kelime)


################################################################ optimizations for the  algorithm
cumle = input("Bir cümle girin: ").lower()
kelimeler = sorted(cumle.split())

print(*kelimeler, sep="\n")
