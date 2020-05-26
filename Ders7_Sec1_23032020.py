# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 09:54:21 2020

@author: Gözde Mihran Altınsoy
"""

print("Merhaba")

import math

print(math.factorial(5))
try:
    print(math.factorial(4))
    print("Hata oluşmadı")
except:
    print("Geçersiz değer")

print(help(math))

print(math.pow(10, 2))
print(10**2)

import mevsimlermodul
print(help(mevsimlermodul))

mevsimlermodul.ilkmevsim()
print(mevsimlermodul.ilkmevsimgetir())

print(mevsimlermodul.mevsimler)

mevsimlermodul.mevsimsayisi()

mevsimsayi=mevsimlermodul.mevsimsayisigetir()
print("Mevsim sayısı:",mevsimsayi)

from rastgele import *

sirala()

liste=rastgelesayi(10, 20, 5)
liste.sort()
print(liste)


from sozlukmodul import *

print(sozluk.keys())
sozlukislem()


