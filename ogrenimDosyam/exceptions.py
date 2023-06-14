
try:
    sayi = int(input("Sayı Giriniz : "))

except ValueError:
    print("Tip uyuşmazlığı. Lütfen sayı giriniz")

except ZeroDivisionError:
    print("Payda sıfır olamaz.")

except:
    print("Bir hata oluştu. Lütfen tekrar deneyiniz.")
print("Bitti")