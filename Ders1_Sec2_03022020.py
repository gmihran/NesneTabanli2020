# -*- coding: utf-8 -*-
"""
Created on Mon Feb  3 15:30:01 2020

@author: gozdemihranaltinsoy
"""

a=10
print(a)
kelime="Beykoz"
print(kelime)
b=10.5
print(b)
b=15
b="B"
a=True
print(a,b)

#Klavyeden girilen değeri ekrana
#yazdıralım
kelime=input("Kelime:")
#input ile klavyeden okunan bütün değerler
#str olarak saklanır
print(kelime)

eşya="Kalem"
print(eşya)

sayı=int(input("Sayı:"))
print(sayı)

sayı=eval(input("Sayı:"))
#Girilen değerin içeriğine göre 
#değişken tipini seçer. (str olamaz)
#eval kullanabilmemiz için 
#sayı olmak zorundadır
print(sayı)

#%%
#Klavyeden girilen sayının 5'e bölümünden
#kalanını ekrana yazdıralım
sayi=int(input("Sayı:"))
print("Kalan:",sayi%5)

#Eğer sayının 5'e bölümünden kalan 0 ise 
#"bölünür", değil ise "bölünmez" yazdıralım
if sayi%5==0:
    print("bölünür")
else:
    print("bölünmez")
    
#Eğer sayı pozitif ise "Pozitif",
#negatif ise "negatif", sıfır ise "sıfır"
#yazdıralım
if sayi>0:
    print("pozitif")
elif sayi<0:
    print("negatif")
else:
    print("sıfır")

#%%
#Girilen kelimenin ilk harfini ekrana yazdıralım
kelime=input("Kelime:")
print(kelime[0])
#ilk karakter = 0.indis değeri ekrana yazdırılır

#%%
#Girilen kelimenin son harfini ekrana yazdıralım
kelime=input("Kelime:")
print(kelime[-1])

#%%
#string parçalama

kelime="BEYKOZ"
#kelime değişkeninde "BEY" ekrana yazdıralım
print(kelime[0:3])
#3.indisteki değer dahil değildir
#son değer indis değerinin 1 fazlasıdır
#ilk değeri yazmazsak ilk karakterden itibaren alır
print(kelime[:3])

#kelime değişkeninde "KOZ" ekrana yazdıralım
print(kelime[3:6])
#son değeri yazmazsak kelimeyi sonuna kadar alır
print(kelime[3:])

#Kelimenin karakter sayısı çift ise ilk harfini,
#tek ise son harfini ekrana yazdıralım
uzunluk=len(kelime)
print("Uzunluk:",uzunluk)
if uzunluk%2==0:
    print(kelime[0])
else:
    print(kelime[-1])
 
try:    
    print(kelime[-7])
except:
    print("Hatalı işlem")   
    #IndexError hata çıktısı yerine bu çıktıyı verir
    #Kelime 6 karakter olduğu için -7 kullanılamaz

#%%
#Kullanıcının girdiği değerin karakter sayısı 0 ise
#"hatalı değer", 0'dan büyükse değerin çıktısını verelim
kelime=input("Kelime:")
if len(kelime)==0:
    print("hatalı değer")
else:
    print(kelime)
    
#%%
#Klavyeden girilen kelimenin 
#5. harfini ekrana yazdıralım
#5. harf (değer) = 4.indis
kelime=input("Kelime:")
print(kelime[4])   
    
#%%    
a=10
b="Merhaba"    
print(a)    
a=str(a)+b  
print(a)  

a,b,kelime,durum=10,20,"Beykoz",True
a,b=b,a
#a=20
#b=10
print(a,b)


#"\n" alt satıra geçmemizi sağlar
#"\t" tab boşluğu (8 karakter boşluk) bırakmamızı sağlar

kelime="Beykoz\tÜniversitesi"
print(len(kelime))


#upper --> Metni büyük harfe dönüştürür
#lower --> Metni küçük harfe dönüştürür

if "beykoz"=="BEYKOZ":
    print("1")
    
if "a" < "b":
    print("a önce gelir")
else:
    print("b önce gelir")

if "cey" < "beykoz":
    print("beykoz")
else:
    print("bey")


#İki kelimeden hangi kelimenin karakter sayısı
#fazla ise o kelimeyi ekrana yazdıralım
#eşit ise herhangi birini yazdıralım
kelime1="Beykoz"
kelime2="Üniversite"
if len(kelime1) < len(kelime2):
    print(kelime2)
else:
    print(kelime1)
















