# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 10:09:25 2020

@author: gozdemihranaltinsoy
"""

#%%
#bloklandırma ile sadece o blokları çalıştırma şansımız vardır.
#Bunun için ctrl + Return veya shift + Return kısayollarını kullanabilirsiniz.

liste1=list()
#boş bir liste1 adında list oluşturuldu

liste2=[]
#boş bir liste2 adında list oluşturuldu

liste3=[1,2,3]
#İçersinde 1,2,3 değerlerini tutan list oluşturuldu

print(liste1,liste2,liste3)

liste1.append("a")
liste1.append("b")
#liste1 listesine "a" ve "b" değerlerini ekledik
print(liste1)

liste2.append(input("Değer:"))
print(liste2)

liste2.append(int(input("Sayı:")))
print(liste2)

liste2.append(eval(input("Reel Sayı:")))
print(liste2)


#sayilar diye boş bir liste oluşturalım
#İçerisine 1 ile 10 arasındaki tüm değerleri atalım
#%%
sayilar=[]
for sayi in range(1,11):
    #artış miktarı yoksa 1'e 1'er artar 
    #range(1,11,1) 
    #başlangıç değeri=1
    #son değeri=11-1=10
    #artış miktarı=1 
    #Artış değeri 1 ise yazmasak da olur.
    sayilar.append(sayi)
print(sayilar)

#teksayilar diye boş bir liste oluşturalım
#İçerisine 51 ile 71 arasındaki değerleri atalım
#%%
teksayilar=[]
for sayi in range(51,72,2):
    teksayilar.append(sayi)
print(teksayilar)

#Kullanıcıdan 10 tane değer isteyelim
#Bu değerlerden sadece pozitif olanları pozitif listesinde tutalım ve ekrana yazdıralım
#%% 
pozitif=[]
for i in range(10):
    sayi=int(input("Sayı:"))
    if sayi>0:
        pozitif.append(sayi)
print(pozitif)


#1 ile 2 arasında bir değer üretip ekrana yazdıralım
#%%
import random
a=random.randint(1,2)
print(a)

#Rastgele üretilen 1-100 arasındaki 20 sayıdan 5'e tam bölünenleri ekrana yazdıralım
#Tüm sayıları da rastgele listesinde tutalım
#%%
import random
#random modülünü(kütüphanesini) projeye dahil ettik
rastgele=[]
#rastgele isminde boş bir liste oluşturduk
print("5'e Tam Bölünenler:")
for i in range(20): #range(0,20)
    #0 ile 19 arasında bir for döngüsü başlattık
    rastgele.append(random.randint(1,100))
    #1 ile 100 arasında rastgele üretilen sayıyı rastgele listesine ekledik
    if rastgele[i]%5==0:
        #rastgele listesinin i.indisindeki değer eğer 5'e tam bölünüyorsa bu if çalışır
        print(rastgele[i])
        #şart doğru ise rastgele listesinin i.indisini ekrana yazdırır
print("Tüm sayılar\n",rastgele) 


#Kullanıcının girdiği string değerin her harfinin sonuna 1'den başlayarak 1'er 1'er artan sayı ekleyelim
#Ör: Kullanıcı "beykoz" girdiyse
#Çıktı: b1e2y3k4o5z6
#Ör: Kullanıcı "kedi" girdiyse
#Çıktı: k1e2d3i4
#%%
kelime=input("Kelime..:")
#1.yöntem:
sifre=[]
sayac=1
for harf in kelime:
    sifre.append(harf)
    sifre.append(sayac)
    sayac+=1
print(sifre)
#2.yöntem:
sifre2=[]
for i in range(0,len(kelime)):
    sifre2.append(kelime[i])
    sifre2.append(i+1)
print(sifre2)

kelimee=sifre[0::2]
print(kelimee)

#Kullanıcıdan adı, numarası bilgisi alalım
#adının ilk 2 harfi, numarasının son 2 harfi, bir tane rastgele özel karakter ve adının son harfini alarak bir şifre oluşturalım
#ozel karakterler ="#.,-_()%&@?+"
#%%
adi=input("Adınız:")
no=input("Numaranız:")
sifre3=[]
sifre3.append(adi[0:2])
sifre3.append(no[len(no)-2:])
#uzunluğunun 2 eksiğindeki indisten başla. 
#Ör: 6 karakterli bir no değeri varsa 4.indisten başlayacak. 
#Son değer belirtilmediği için değerin sonuna kadar alır.
ozel="#.,-_()%&@?+"
sifre3.append(ozel[random.randint(0,len(ozel)-1)])
sifre3.append(adi[len(adi)-1])
#sifre3.append(adi[-1:])
print(sifre3)
strsifre=""

for deger in sifre3:
    print(deger)

#listedeki değeri string bir değişkende tutalım
for deger in sifre3:
    strsifre=strsifre+deger
print(strsifre)

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
hak=6
kelime=["_","_","_","_","_"]
kelimeler=["köpek","kitap","kalem","silgi","araba","sıcak","soğuk","ekran","bahçe","dalga"]
rastkelime=random.choice(kelimeler)
print(rastkelime)

while hak>0:
    print(kelime)
    harf=input("Harf..:")
    kontrol=False
    for i in range(5):
        if harf==rastkelime[i]:
            kelime[i]=rastkelime[i]
            #kelime[i]=harf
            kontrol=True
    if kontrol==False:
        hak-=1
    bilinmeyen=kelime.count("_")
    if bilinmeyen==0:
        break
    print("Kalan hakkınız:",hak)
if bilinmeyen==0:
    print("Tebrikler.Kelime:",rastkelime)
else:
    print("Bilemediniz.Kelime:",rastkelime)


        












