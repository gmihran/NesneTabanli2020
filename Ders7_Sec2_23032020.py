# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 14:48:45 2020

@author: Gözde Mihran Altınsoy
"""

import math

print(help(math))

math.factorial(5)

try:
    print(math.factorial(-5))
    print("Hata oluşmadı")
except:
    print("Hatalı giriş")

print(math.pow(5, 2))

import mevsimler
help(mevsimler)

print(mevsimler.mevsim)
mevsimler.yazdir()

mevsimler.ilkmevsim()

mevsim=mevsimler.ilkmevsimgetir()
print(mevsim)
for i in mevsim:
    print(i)

for i in mevsim:
    print(i,end=",")
    
print()
mevsimler.mevsimsayisi()

mevsimsay=mevsimler.mevsimsayisigetir()
print(mevsimsay)

from kelimemodul import *

print(kelime)
tersyazdir()
ilkkelime2()










