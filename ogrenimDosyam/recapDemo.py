ogrenciler = ["Musa", "Ceren", "Timur", "Gürgil"]

fileToAppend = open("ogrenciler.txt","a")
for ogrenci in ogrenciler:
    fileToAppend.write(ogrenci)
    fileToAppend.write("\n")

fileToAppend.close()