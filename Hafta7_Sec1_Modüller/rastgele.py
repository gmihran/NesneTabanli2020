# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 10:47:18 2020

@author: Gözde Mihran Altınsoy

Bu fonksiyon ile random kütüphanesi ile çalışarak çeşitli karşılaştırmalar yapacağız

"""

import random

def rastgelesayi(x,y,miktar):
    sayilar=[]
    #sayilar=list()
    
    if x>y:
        x,y=y,x
    #print(x,y)
    for i in range(1,miktar+1):
        sayilar.append(random.randint(x, y))
    #print(sayilar)
    return sayilar

def sirala():
    sayilar=rastgelesayi(1, 20, 5)
    sayilar.sort()
    #sayilar.sort(reverse=False)
    #False varsayılan değerdir
    #Küçükten büyüğe sıralar
    
    print(sayilar)
    #sayilar.sort(reverse=True)
    #Büyükten küçüğe sıralar
    return sayilar
    
def sayikontrol():
    sayilar=sirala()
    while True:
        sayi=int(input("1-20 arasında sayı giriniz:"))
        if sayi>=1 and sayi<=20:
            break
    if sayi in sayilar:
        print("Tebrikler")
    else:
        print("Üzgünüz")
    
def sayikontrol2():
    liste=[]
    sayilar=sirala()
    print(liste)
    for i in range(1,6):
        while True:
            sayi=int(input("Sayı giriniz:"))
            if sayi>=1 and sayi<=20:
                break
            else:
                print("Sayı 1 ie 20 arasında olmalıdır")
        liste.append(sayi)
    sayac=0
    for i in range(0,5):
         if liste[i] in sayilar:
             sayac+=1
    print(sayac)
sayikontrol2()        


#sirala()


