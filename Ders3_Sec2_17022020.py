# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 15:07:02 2020

@author: gozdemihranaltinsoy
"""
#%%
#bloklandırma ile sadece o blokları çalıştırma şansımız vardır.
#Bunun için ctrl + Return veya shift + Return kısayollarını kullanabilirsiniz.

liste1=[]
#liste1 adında boş bir liste oluşturuldu

liste2=list()
#liste2 adında boş bir liste oluşturuldu
liste2.append(2)
#2 sayısı liste2 listesine eklendi
liste2.append("beykoz")
#"beykoz" listeye eklendi
liste2.append(15.6)
#15.6 değeri listeye eklendi
liste2.append(input("Değer:"))
#kullanıcının girdiği değeri str türünde liste2'ye eklendi
liste2.append(True)
#true bool değerini listeye eklendi
liste2.append(eval(input("Sayı:")))
#float veya int türünde değer listeye eklendi. Ör 5 girerse int, 5.7 girerse float türünde saklar

print("3"==3)
a=3
b="3"
print(a==b)

liste3=[1,2,3,"a",True]
#5 elemanlı liste3 adında list oluşturuldu

#1 ile 10 arasındaki sayıları sayılar listesine ekleyelim
#%%
sayilar=[]
for i in range(1,11):
    sayilar.append(i)
    print(sayilar)

#51 ile 71 arasındaki tek sayıları teksayilar listesine ekleyip, listeyi ekrana yazdıralım
#%%
teksayilar=[]
for i in range(51,72,2):
    #başlangıç değeri: 51
    #bitiş değeri: 72-1=71
    #artış miktarı: 2
    #artış miktarı belirtilmezse 1 olarak kabul edilir
    teksayilar.append(i)
print(teksayilar)


#Kullanıcının girdiği 10 tane değerden sadece pozitif olanları ekrana yazdırıp, tüm listeyi sayilar listesine atayıp ekrana yazdıralım

#Burada da kullanıcının girdiği değerler listeye eklenip, sadece pozitif olanları ekrana yazdıralacak
sayilar=[]
for i in range(10):
    #başlangıç değeri:0
    #bitiş değeri:9
    sayilar.append(eval(input("Sayı:")))
    
print("Pozitif sayılar:")
for sayi in sayilar:
    if sayi>0:
        print(sayi)
print("Tüm sayılar") 
print(sayilar)
#Burada liste yazdırıldı


#0 ile 1 arasında bir değer üretip ekrana yazdıralım
#%%
import random
rastgele=random.randint(0,1)
print(rastgele)
#print(random.randint(0,1))

#Rastgele üretilen 1-100 arasındaki (random sayı aralığı 1-100) 20 sayıdan 5'e tam bölünenleri ekrana yazdıralım
#Tüm sayıları da rastgele listesinde tutalım ve bu sayıları ekrana yazdıralım
#%%
import random
rastgele=[]
for i in range(20):
    rastgele.append(random.randint(1,100))
    if rastgele[i]%5==0:
        print(rastgele[i])
print(rastgele)

#Kullanıcının girdiği string değerin her harfinin sonuna 1'den başlayarak 1'er 1'er artan sayı ekleyelim
#Ör: Kullanıcı "beykoz" girdiyse
#Çıktı: b1e2y3k4o5z6
#Ör: Kullanıcı "kedi" girdiyse
#Çıktı: k1e2d3i4
#%%
kelime=input("Kelime..:")
yenikelime=[]
for i in range(0,len(kelime)):
    yenikelime.append(kelime[i])
    yenikelime.append(i+1)
print(yenikelime)
ykelime=""
for harf in yenikelime:
    ykelime=ykelime+str(harf)
print(ykelime)


#Kullanıcıdan adı, numarası bilgisi alalım
#adının ilk 2 harfi, numarasının son 2 harfi, bir tane rastgele özel karakter ve adının son harfini alarak bir şifre oluşturalım
#ozel karakterler ="#.,-_()%&@?+"
#%%
import random
ozel="#.,-_()%&@?+"
karakter=random.choice(ozel)
sifre=""
adi=input("Adınız:")
no=input("Numaranız:")
"""
sifre=sifre+adi[0:2]
sifre=sifre+no[len(no)-2:]
sifre=sifre+karakter
sifre=sifre+adi[-1:]
print(sifre)
"""
sifre=adi[0:2]+no[len(no)-2:]+karakter+adi[-1:]
print(sifre)

#Adam asmaca oyunu
#İçerisinde 10 adet 5 harfli kelimeler tutan bir liste tanımlayalım
#Bu listeden rastgele bir kelime seçelim
#Kullanıcının tek tek harf girmesini sağlayıp bu harfler kelimede var mı kontrol edelim
#Kullanıcının 6 yanlış harf girme hakkı var
#Çıktı
# _ _ _ _ _
#Ör:kelime köpek ise ve kullanıcı "k" girdiyse
#Çıktı
# k _ _ _ _ k
#Ör:kullanıcı e harfini girdiyse
# k _ _ _ e k
#%%
import random
kelimeler=["kalem","silgi","kağıt","köpek","sevgi","yunus","balık","çiçek","yusuf","mısra"]
liste=["_","_","_","_","_"]
hak=6
kelime=random.choice(kelimeler)
print(kelime)
while hak>0:
    kontrol=False
    print(liste)
    harf=input("Harf..:")  
    for i in range(0,len(kelime)):
        if harf==kelime[i]:
            liste[i]=harf
            #liste[i]=kelime[i]
            kontrol=True
    if kontrol==False:
        hak-=1
        print("Kalan hakkınız:",hak)
    if liste.count("_")==0:
        break
if liste.count("_")==0:
    print("Tebrikler. Kelime:",kelime)   
else:
    print("Bilemediniz. Kelime:",kelime)

    
    
    




