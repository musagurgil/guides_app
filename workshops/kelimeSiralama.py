cumle = input("Bir cümle girin: ").lower()
kelimeler = sorted(cumle.split())

print(*kelimeler, sep="\n")
