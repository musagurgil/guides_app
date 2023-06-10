sehirler = ["Ankara", "İstanbul", "İzmir"]

for sehir in sehirler:
    if sehir == "İstanbul":
        continue
    print(sehir + " İçin Kod =" + sehir[0:3])
    print("********************************")

for x in range(1, 50, 2):
    print(x + 1)
