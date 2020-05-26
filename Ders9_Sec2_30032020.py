# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 14:55:58 2020

@author: Gözde Mihran Altınsoy
"""

import sqlite3
con=sqlite3.connect("kitapdunyasi.db")
cursor=con.cursor()

def tabloolustur():
    #cursor.execute("CREATE TABLE kitaplik(isim TEXT,yazar TEXT,yayinevi TEXT,sayi INT)")
    #Eğer bu tablo veritabanında mevcut ise 
    #OperationalError: table kitaplik already exists
    #hata mesajı alırız
    cursor.execute("CREATE TABLE IF NOT EXISTS kitaplik(isim TEXT,yazar TEXT,yayinevi TEXT,sayi INT)")
    #IF NOT EXISTS ile CREATE TABLE (tablo oluşturma) işlemi yaparsak tablo var ise hata mesajı vermez. Yoksa tabloyu oluşturur.
    con.commit()

def veriekle():
    cursor.execute("INSERT INTO kitaplik VALUES('İstanbul Hatırası','Ahmet Ümit','Everest',561)")
    #VALUES() ifadesindeki ) parantez kapama işlemini gerçekleştirmezsek;
    #OperationalError: incomplete input
    #hatasını alırız
    con.commit()

def veriekle2(kitapadi,yazaradi,yayinevi,sayfa):
    cursor.execute("INSERT INTO kitaplik VALUES(?,?,?,?)",(kitapadi,yazaradi,yayinevi,sayfa))
    con.commit()
    
def verial():
    cursor.execute("SELECT * FROM kitaplik")
    data=cursor.fetchall()
    print(data)
    
    for i in data:
        print(i)
        
    for i in data:
        for j in i:
            print(j)
    
    for i in data:
        print("Kitap adı:",i[0])
        print("Yazar adı:",i[1])
        print("Yayınevi:",i[2])
        print("Sayfa sayısı:",i[3])
        
    print()
    
    for i in data:
        kitaplar.append(i[0])
        yazarlar.append(i[1])
        yayinevleri.append((i[2]))
        sayilar.append(i[3])
    print("Kitaplar:",kitaplar,"\nYazarlar:",yazarlar,"\nYayınevleri:",yayinevleri,"\nSayfa Sayıları:",sayilar)

def verial2():
    cursor.execute("SELECT isim,yazar FROM kitaplik")
    veri=cursor.fetchall()
    print(veri)
    
def verial3(kitapadi):
    cursor.execute("SELECT * FROM kitaplik WHERE isim=?",(kitapadi,))
    #Python ile tek bir değişkeni sorguya dahil etmek istediğimizde mutlaka değişken isminden sonra , konulmalıdır.
    #ProgrammingError: Incorrect number of bindings supplied. The current statement uses 1, and there are 8 supplied.
    #hatasının olmaması için (kitapadi,) kitapadi değişkeninden sonra virgün (,) eklenmelidir.
    #OperationalError: no such column: kitap
    #sütun ismini isim yerine kitap olarak yazdığımızda bu tablomuzda kitap alanı olmadığı için bu hata oluşur.
    veri=cursor.fetchall()
    print(veri)

def verial4(ilksayfa,sonsayfa):
    cursor.execute("SELECT * FROM kitaplik WHERE sayi BETWEEN ? AND ?",(ilksayfa,sonsayfa))
    data=cursor.fetchall()
    print(data)

def verial5(kitapadi,yazaradi):
    cursor.execute("SELECT * FROM kitaplik WHERE isim=? AND yazar=?",(kitapadi,yazaradi))
    data=cursor.fetchall()
    print(data)
    
def veriguncelle():
    cursor.execute("UPDATE kitaplik SET sayi=561 WHERE yayinevi='Everest'")
    con.commit()
    
    
def veriguncelle2(eskikitapadi,yenikitapadi):
    cursor.execute("UPDATE kitaplik SET isim=? WHERE isim=?",(yenikitapadi,eskikitapadi))
    con.commit()
    
def verisil():
    cursor.execute("DELETE FROM kitaplik WHERE isim='Çalıkuşu'")
    con.commit()    
    
def verisil2(kitapadi):
    cursor.execute("DELETE FROM kitaplik WHERE isim=?",(kitapadi,))
    con.commit()
    
def tablosil():
    cursor.execute("DROP TABLE kitaplik")
    con.commit()
    

tabloolustur()

veriekle()

veriekle2("Çalıkuşu","Reşat Nuri Güntekin","İnkılap Kitapevi",509)


kitapadi=input("Kitap Adı:")
yazar=input("Yazar Adı:")
yayinevi=input("Yayınevi:")
sayfa=int(input("Sayfa sayısı:"))
veriekle2(kitapadi,yazar,yayinevi,sayfa)

veriekle2("Olasılıksız","Adam Fawer","April Yayıncılık",475)

kitaplar=[]
yazarlar=[]
yayinevleri=[]
sayilar=[]

verial()

print()
verial2()

print()
verial3("Çalıkuşu")

kitap=input("Kitap adı:")
verial3(kitap)

kitap="Olasılıksız"
verial3(kitap)

print()
verial4(500,561)

print()
verial5("İstanbul Hatırası","Ahmet Ümit")

veriguncelle()

kitaplar=[]
yazarlar=[]
yayinevleri=[]
sayilar=[]
verial()

veriguncelle2("Çalıkuşu","Acımak")
veriguncelle2("Acımak","Çalıkuşu")


verisil()

kitaplar=[]
yazarlar=[]
yayinevleri=[]
sayilar=[]
verial()

verisil2("Olasılıksız")

kitaplar=[]
yazarlar=[]
yayinevleri=[]
sayilar=[]
verial()

tablosil() #Tüm tablo silindi


con.close()








