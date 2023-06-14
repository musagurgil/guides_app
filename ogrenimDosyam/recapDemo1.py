# ************************************************************************************************TRAFIK ISIGI
# lights = ["red", "green", "yellow"]

# currentLight = lights[0]

# print(currentLight)

# if currentLight == "red":
#     print("STOP!")

# elif currentLight == "yellow":
#     print("READY!")
# elif currentLight == "green":
#     print("GO!")


# ************************************************************************************************YILDIZ YAZDIRIMI
# sayi = int(input("Kaç yıldız yazılsın ?"))
# yildiz = ""

# for x in range(1, sayi + 1):
#     yildiz = yildiz + "*"
#     print(yildiz)


# ************************************************************************************************ASAL SAYI YAZDIRIMI

sayi = int(input("Bir sayı girin: "))
asalMi = True
for x in range(2, sayi):
    if (sayi % x) == 0:
        asalMi = False
        break

if asalMi == True:
    print("ASAL")
else:
    print("ASAL DEGİL")
