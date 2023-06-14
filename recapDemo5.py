import syslog

liste = ['a', 'b', 'c', 'd', 'e', 0, 1, 2, 3, 4, 5, 6, '6']

for x in liste:
    try:
        print ("Sayı: "+ str(x))
        sonuc = 1/int(x)
        print("Sonuç :" + str(sonuc))
    except:
        print(str(x) + " Hesaplanamadı. ")