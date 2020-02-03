# -*- coding: utf-8 -*-
"""
Created on Mon Feb  3 10:40:43 2020

@author: gozdemihranaltinsoy
"""

a=10
b=30
print(a)
print(b)
toplam=a+b
print(a+b)
print(toplam)
print("Toplam:",toplam)
if a>b:
    print("a değeri büyüktür")
elif b>a:
    print("b değeri büyüktür")
else:
    print("a değeri b'ye eşittir")
print("Merhaba")

#a değeri b değerine tam bölüyor ise
#ekrana "tam bölünür" çıktısı verelim
#a % b == 0
if a%b==0:
    print("tam bölünür")
    
#a değeri b değerine tam bölüyor ise
#ekrana "tam bölünür" çıktısı verelim
#tam bölünmüyor ise "bölünmez"
#çıktısını versin
#a % b == 0
#%%
a=10
b=5
if a%b==0:
    print("tam bölünür")
else:
    print("bölünmez")


#%%
#Eğer sayı 2'ye tam bölünüyor ise
#...." sayısı 2'ye bölünür", 
#bölünmüyor ise
#..." sayısı 2'ye bölünmez" yazdıralım
sayi=6
if sayi%2==0:
    print(sayi," sayısı 2'ye bölünür")
else:
    print(sayi," sayısı 2'ye bölünmez")

#Girilen kelimeyi ekrana yazdıralım
kelime=input("Kelime:")

#Klavyeden hangi değer girilirse girilsin
#input ile klavyeden alınan değerler
#string türüyle saklanır.

print(kelime)

#Girilen sayının tek veya çift olduğunu
#ekrana yazdıralım

sayi=int(input("Sayı:"))
#Klavyeden girilen ve okunan değer 
#int veri türüne dönüştürüldü 
print(sayi)
if sayi%2==0:
    print("Çift")
else:
    print("Tek")
#%%
#Klavyden girilen sayının 
#pozitif, negatif ve sıfır olma durumunu 
#ekrana yazdıralım
sayi=int(input("Sayı:")) 
if sayi>0:
    print("Pozitif")
elif sayi<0:
    print("Negatif")
else:
    print("Sıfır")
#%%
#eval: Girilen değerin içeriğine göre
#değişken tipini ayarlar (int,float)
#str veri türünde eval kullanılamaz
deneme=eval(input("Değer:"))
print(deneme)

#%%
#Klavyeden girilen kelimenin 
#ilk harfini ekrana yazdıralım
kelime=input("Kelime:")
print(kelime[0])

#%%
#Klavyeden girilen kelimenin 
#5. harfini ekrana yazdıralım
#5. harf (değer) = 4.indis
kelime=input("Kelime:")
print(kelime[4])
if (kelime=="beykoz"):
    print("Evet")
print(kelime[1])

#%%
#Klavyeden girilen kelimenin 
#son harfini ekrana yazdıralım
kelime=input("Kelime:")
print(kelime[-1])    


#%%
#Klavyeden girilen kelimenin 
#son harfini ekrana yazdıralım
kelime=input("Kelime:")
print(kelime[-1])


#%%
if (len(kelime)==0):
    print("Değer girilmedi")
if (len(kelime)>=9):
    print(kelime[-9])
try:
    print(kelime[-9]) 
except:
    print("Hatalı giriş yapıldı")
    #kelimenin 9 karakterden daha az 
    #karaktere sahip olması durumunda 
    #IndexError hatasını yakalar


#%%
#Klavyeden girilen kelimenin karakter 
#sayısı tek ise kelimenin 1. harfini,
#çift ise kelimenin son harfini 
#ekrana yazdıralım
kelime=input("Kelime:")
#Bir kelimenin uzunluğunu öğrenmek için
#len() fonksiyonu kullanılır
print(len(kelime))
uzunluk=len(kelime)
print("Kelimenin uzunluğu:",uzunluk)
if uzunluk%2==0:
    print(kelime[-1])
else:
    print(kelime[0])

#%%
#String parçalama:
kelime="BEYKOZ"

#"BEY" çıktısını verelim
print(kelime[0:3])
#Son indis değerinin 1 fazlasını yazarız
#Çıktıda 3. indis dahil değildir

#"KOZ" çıktısını verelim
print(kelime[3:6])
#Son indis değerinin 1 fazlasını yazarız

#"EY" çıktısını verelim
print(kelime[1:3])    

#%%
a,b,kelime=10,20,"Beykoz"
a,b=b,a
print("a:",a)
print("b:",b)

print("a:",a,"\tb:",b)
#"\n" alt satıra geçmemizi sağlar
#"\t" tab boşluğu (8 karakter boşluk) bırakmamızı sağlar

#upper --> Metni büyük harfe dönüştürür
#lower --> Metni küçük harfe dönüştürür

#"beykoz"=="BEYKOZ"
#"A" < "B"
if "a"<"b":
    print("a harfi önce gelir")
else:
    print("b harfi önce gelir")

if "bey"<"beykoz":
    print("bey")
else:
    print("beykoz")










