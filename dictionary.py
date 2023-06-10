sozluk ={
    "book" : "kitap",
    "table" : "masa",
    "mouse" : "fare"
}


# sozluk2 = dict(kitap = "book", masa = "table") #ikinci bir sozluk tanimi.

# sozluk["book"] = "kitap 1"   #sozluge deger ekleme
# sozluk["pencil"] = "kalem"    #sozluge deger ekleme

del(sozluk["table"])
print(len(sozluk))
print (sozluk["book"])