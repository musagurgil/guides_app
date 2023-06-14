import sqlite3

connection = sqlite3.connect("chinook.db") # veritabanı bağlantısı yapıldı.

def selectOperasyonlari():

    #cursor = connection.execute("select * from customers") # custormers tablosundaki tüm verileri getirdi.


    #---------------------------------------------------------------- Prague veya Berlin şehirlerindeki kişileri İsme göre sıralamakta. 
    # cursor = connection.execute("""select FirstName, LastName from customers where city = 'Prague' or city = 'Berlin' order by FirstName""") 
    # for row in cursor:
    #     print("First Name = "+row[0],"|","Last Name =" +row[1])
    #     print("***")
    #----------------------------------------------------------------

    #---------------------------------------------------------------- 1'den çok müştrei bulunan şehri z-a ya göre sıralamakta
    # cursor = connection.execute("select city,count(*) from customers group by city having count(*)>1 order by count(*) desc") 
    # for row in cursor:
    #     print("City = "+row[0],"|","Count = "+str(row[1]))
    #     print("***")
    #----------------------------------------------------------------

    #---------------------------------------------------------------- İsmi "Ja" ile biten kişileri listeler.
    # cursor = connection.execute("select FirstName,LastName from customers where FirstName like '%ja'")
    # for row in cursor:
    #     print("First Name = "+row[0],"|","Last Name =" +row[1])
    #----------------------------------------------------------------

    connection.close() # veritabanı bağlantısını kapatıldı.

selectOperasyonlari()

#---------------------------------------------------------------- customers tablosuna veri girişi yapıldı.
# def insertCustomer():
#     connection = sqlite3.connect("chinook.db")
#     connection.execute("insert into customers(firstName,lastName,City,email) values('Musa','Gürgil','Ankara','musagurgil@gmail.com')")
#     connection.commit()
#     connection.close()
# insertCustomer()
#----------------------------------------------------------------

#---------------------------------------------------------------- customers tablosundaki şehri 'Ankara' olan kayıtlar 'İstanbul' ile değiştirildi.
# def updateCustomer():
#     connection = sqlite3.connect("chinook.db")
#     connection.execute("update customers set city='İstanbul' where city='Ankara'")
#     connection.commit()
#     connection.close()
# updateCustomer()
#----------------------------------------------------------------

#---------------------------------------------------------------- customers tablosundaki id'si 60 olan kayıtı siliyor.
# def deleteCustomer():
#     connection = sqlite3.connect("chinook.db")
#     connection.execute("delete from customers where customerid=60")
#     connection.execute("delete form customers where city 'İstanbul' or country='Germany'") # İstanbul veya ülkesi Almanya olan kayıtı siliyor.
#     connection.commit()
#     connection.close()
# deleteCustomer()
#----------------------------------------------------------------

#---------------------------------------------------------------- iki farklı veritabanıdaki verileri yazdırmak
def joinOperasyonlari():
    connection = sqlite3.connect("chinook.db")
    cursor = connection.execute("select albums.Title, artists.Name from artists inner join albums on artists.ArtistId = albums.ArtistId")

    for row in cursor:
        print("Title: "+row[0]+" Name: "+row[1])

    connection.close()
joinOperasyonlari()
#----------------------------------------------------------------

#asc = A-Z
#desc = Z-A

# %a% = içinde a bulunan 
# a% = a ile başlayan
# %a = a ile biten