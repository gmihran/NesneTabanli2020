# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 17:13:37 2020

@author: Gözde Mihran Altınsoy
"""


a,b,c,d=6,5,2,4

#x,y,z,t=2
#TypeError: cannot unpack non-iterable int object


a="Beykoz"
b=a
a+="Üniversitesi"
print(a,b)

vize,final,ödev=60,50,70
ortalama=(vize+final+ödev)/3
print(ortalama)


a=10
b=15
a*=b #a=a*b #a=150
b+=a #b=b+a #b=165
print(a,b)

isim=250
sayı="1"
durum="True"

print(type(isim))
print(type(sayı))
print(type(durum))
"""
<class 'int'>
<class 'str'>
<class 'str'>
"""


sayi=35
a=sayi%4
print(a)

deger="1234"
print(deger[-1])

deger=1234
print(deger%10)

deger=1234
deger=str(deger)
print(deger[3])
print(int(deger)%10)

pi=3
r=5.3
cevre=2*pi*r
alan=pi*(pow(r,2))
print(cevre,alan)

sayilar = [13,21,20,67,35,19,14,90,85,11,45,302,205,2,39]
sayac=0
for sayi in sayilar:
   if (sayi%5== 0):
      sayac=sayac+1
print(str(sayac))

import math
#from math import *
print(pow(5,2))
print(math.floor(5.2))


liste=[1,2,3,4]
liste[0]=5
print(liste)

demet=(1,2,3,4)
#demet[0]=5
print(demet)

sozluk={"computer":"bilgisayar","pencil":"kalem","water":"su"} 
print(sozluk.get("su"))  #None
#print(sozluk["su"]) #KeyError: 'su'

sayilar=[4,2,10,3]
sayilar.sort(reverse=True)
print(sayilar)

sayilar.sort()
print(sayilar)

import random
sayi=random.randint(1,2) 
print(sayi)

deger=input("Değer:")
print(type(deger)) #<class 'str'>
