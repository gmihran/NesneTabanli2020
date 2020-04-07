# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 12:30:58 2020

@author: Gözde Mihran Altınsoy
"""

#Soru-1:
a,b,c,d=6,5,2,4
#x,y,z,t=2
#TypeError: cannot unpack non-iterable int object

#Soru-2:
a="Beykoz"
b=a
a+="Üniversitesi"
print(a,b)
#BeykozÜniversitesi,Beykoz

#Soru-3:
vize,final,ödev=60,50,70
ortalama=(vize+final+ödev)/3
print(ortalama)

#Soru-4:
a=10
b=15
a*=b #a=a*b #a=150
b+=a #b=b+a #b=165
print(a,b)
#150,165

#Soru-5:
isim=250
sayı="1"
durum="True"
print(type(isim),type(sayı),type(durum))
#<class 'int'> <class 'str'> <class 'str'>
#int,str,str

#Soru-6:
sayi=35
a=sayi%4
print(a)
#3

#Soru-8:
deger=1234
print(pow(deger,1/10))
#print(len(deger)-1)
#deger="1234"
#print(deger[3]) 
#string objelerde parçalama işlemi yapılır. int için bu geçerli değildir
#print(deger[-1])
print(deger%10)

#Soru-9:
pi=3
r=5.3
cevre=2*pi*r
alan=pi*(pow(r,2))
print(cevre,alan)

#Soru-11:
sayilar = [13,21,20,67,35,19,14,90,85,11,45,302,205,2,39]
sayac=0
for sayi in sayilar:
   if (sayi%5== 0):
      sayac=sayac+1
print(str(sayac))
#6

#Soru-12:
import math
print(pow(5,2)) #pow hata vermedi. Bu soruya doğru yanıtını da yanlış yanıtını da kabul edeceğim
#print(floor(5.2)) #floor fonksiyonu hata verir
print(math.floor(5.2))

demet=(1,2,3)
#demet[0]=5

liste=[1,2,3]
liste[0]=5
print(liste)

sozluk={"computer":"bilgisayar","pencil":"kalem","water":"su"} 
print(sozluk.get("su"))  #None

#print(sozluk["su"]) #KeyError: 'su'


sayilar=[4,2,10,3]
sayilar.sort(reverse=True) #Tersine sırala-> Büyükten küçüğe sıralar
print(sayilar)
#[10, 4, 3, 2]

import random
sayi=random.randint(1,2) 
print(sayi)

deger=input("Değer:")
print(type(deger))


"6"
pow Doğru Yanlış



