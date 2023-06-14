f = open("musteriler.txt")
# print(f.read())
print(("********************************"))

for l in f:
    print(l)
f.close()
# r = Read
# a = Append
# w = Write ,dosyanın üzerine yazar
# x = Create

# fileToAppend = open("ogrenciler.txt","a")
# fileToAppend.write("\n")
# fileToAppend.write("Musa")
# fileToAppend.close()

import os
if os.path.exists("ogrenciler.txt"):
    os.remove("ogrenciler.txt") # remove obsolete files
else:
    print("Dosya bulunamadı")

os.rmdir("empty")