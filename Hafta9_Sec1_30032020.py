# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 10:00:00 2020

@author: Gözde Mihran Altınsoy
"""

import sqlite3
con=sqlite3.connect("kitapevi.db")
cursor=con.cursor()

def tabloolustur():
    #cursor.execute("CREATE TABLE kitaplik (isim TEXT,yazar TEXT,sayi INT)")
    
    #OperationalError: table kitaplik already exists 
    #kitaplik isimli tablo bir kere oluşturulsa tekrar aynı kodu çalıştırmamız çalışma zamanı hata verir. Hata da bu tablonun zaten var olduğunu ve üzerine yazılamayacağı belirtiliyor.
    cursor.execute("CREATE TABLE IF NOT EXISTS kitaplik (isim TEXT,yazar TEXT,yayinevi TEXT,sayi INT)")
    #Bu tablo varsa tekrar oluşturamayacağı için hata vermemesi adına IF NOT EXISTS yazdık. Bu tablo varsa hata oluşmayacaktır, yoksa tablo oluşturulacaktır.

def veriekle():
    cursor.execute("INSERT INTO kitaplik VALUES('İstanbul Hatırası','Ahmet Ümit','Everest',261)")
    con.commit()

def veriekle2(kitapadi,yazaradi,yayinevi,sayi):
    cursor.execute("INSERT INTO kitaplik VALUES(?,?,?,?)",(kitapadi,yazaradi,yayinevi,sayi))
    con.commit()
    print("Kayıt eklendi.")
   
def verial():
    cursor.execute("SELECT * FROM kitaplik")
    data=cursor.fetchall()
    print(data)
    for i in data:
        print(i)
    for i in data:
        for j in i:
            print(j,end=",")
        print()
    for i in data:
        print("\nKitap Adı:",i[0],"\nYazar adı:",i[1],"\nYayınevi:",i[2],"\nSayfa:",i[3])
    
    sayac=0
    for i in data:
        isimler.append(i[0])
        yazarlar.append(i[1])
        yayinevleri.append(i[2])
        sayfasayilari.append(i[3])
        print("\nKitap Adı:",isimler[sayac],"\nYazar adı:",yazarlar[sayac],"\nYayınevi:",yayinevleri[sayac],"\nSayfa:",sayfasayilari[sayac])
        sayac=sayac+1
        
        
def verial2():
    cursor.execute("SELECT * FROM kitaplik WHERE isim='İstanbul Hatırası'")
    #kitap ismi İstanbul Hatırası olan kitabın tüm alan verileri çekildi.
    data=cursor.fetchall()
    print(data)

def verial3():
    cursor.execute("SELECT isim,sayi FROM kitaplik WHERE isim='İstanbul Hatırası'")
    #kitap ismi İstanbul Hatırası olan kitabın isim ve sayi verileri çekildi.
    data=cursor.fetchall()
    print(data)
    
def verial4(kitapadi):
    cursor.execute("SELECT * FROM kitaplik WHERE isim=?",(kitapadi,))
    #Eğer sorgudan sonra sorguya dahil edilecek bir değişken varsa o değişkenden sonra , koyulur. Yoksa 
    #ProgrammingError: Incorrect number of bindings supplied. The current statement uses 1, and there are 5 supplied.
    #hatası oluşur.
    data=cursor.fetchall()
    print(data)

def verial5(kitapadi,sayfa):
    cursor.execute("SELECT * FROM kitaplik WHERE isim=? AND sayi=?",(kitapadi,sayfa))  
    data=cursor.fetchall()
    print(data)
    
#Kendisine gönderilen sayıları alıp bu sayfa sayısı arasındaki kitapları ekrana yazdıran Python kodunu Sql sorgusu ile birlikte yazınız. (BETWEEN arasında durumunu ifade eder)
def verial6(sayfa1,sayfa2):
    cursor.execute("SELECT * FROM kitaplik WHERE sayi BETWEEN ? AND ?",(sayfa1,sayfa2))
    #Lcursor.execute("SELECT * FROM kitaplik WHERE sayi>=? AND sayi<=?",(sayfa1,sayfa2))
    veri=cursor.fetchall()
    print(veri)

def veridegistir():
    cursor.execute("UPDATE kitaplik SET sayi=214 WHERE isim='Yaban'")
    con.commit()
    
def veridegistir2(eskikitapadi,yenikitapadi):
    cursor.execute("UPDATE kitaplik SET isim=? WHERE isim=?",(yenikitapadi,eskikitapadi))
    con.commit()


def verisil(kitapadi):
    cursor.execute("DELETE FROM kitaplik WHERE isim=?",(kitapadi,))
    con.commit()
    
    
def tumveriyisil():
    cursor.execute("DELETE FROM kitaplik")
    con.commit()

def tablosil():
    cursor.execute("DROP TABLE kitaplik")
    con.commit()
    
    
tabloolustur()
veriekle()

kitap=input("Kitap adı:")
yazar=input("Yazar adı:")
yayinevi=input("Yayınevi:")
sayfa=int(input("Sayfa sayısı:"))
veriekle2(kitap,yazar,yayinevi,sayfa)

veriekle2("Simyacı","Paulo Coelho","Can Yayınları",184)

veriekle2("Yaban","Yakup Kadri","İletişim Yayıncılık",214)

data=[]
isimler=[]
yazarlar=[]
yayinevleri=[]
sayfasayilari=[]
#Eğer değişkenler burada (ana fonksiyon) içinde tanımlanırsa public olur ve diğer fonksiyonlar içinde kullanılabilir. Ve değişkenler içinde program çalıştığı sürece kalıcı değişiklik oluşur.

verial()

print(isimler[0])

verial2()

verial3()

verial4("Yaban")

verial5("Simyacı",250) #Adı Simyacı olan ve sayfa sayısı 250 olan bir kitap olmadığı için [] boş liste çıktısı alırız
verial5("Simyacı",184) ##Adı Simyacı olan ve sayfa sayısı 184 olan bir kitap olduğu için o kitabın çıktısını 

print()
verial6(210,261)

veridegistir()
veridegistir2("Yaban","Ankara") #kitap adı Yaban olan kitabın kitap adını Ankara yapar

veridegistir2("Ankara","Yaban") #kitap adı Ankara olan kitabın kitap adını Yaban yapar

data=[]
isimler=[]
yazarlar=[]
yayinevleri=[]
sayfasayilari=[]
verial()

verisil("Simyacı") #Simyacı ismine sahip olan tüm kitaplar silindi

data=[]
isimler=[]
yazarlar=[]
yayinevleri=[]
sayfasayilari=[]
verial()

tumveriyisil() #Tablomuz içindeki tüm veriler silindi

data=[]
isimler=[]
yazarlar=[]
yayinevleri=[]
sayfasayilari=[]
verial()

tablosil() #Tüm tablomuz silindi

con.close()

