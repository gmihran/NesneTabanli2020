# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 15:09:16 2020

@author: Gözde Mihran Altınsoy
"""

import random

def rastgeleolustur():
    sayi=random.randint(1, 10)
    print(sayi)

def rastgeleolustur2(x,y):
    if x>y:
        x,y=y,x
    sayi=random.randint(x, y)
    print(sayi)

def rastgeleolustur3(x,y,miktar):
    sayilar=[]
    #sayilar=list()
    if x>y:
        x,y=y,x
    for i in range(1,miktar+1):
        sayilar.append(random.randint(x, y))
    print(sayilar) 
    return sayilar

def sirala():
    sayilar=rastgeleolustur3(1, 10, 5)
    sayilar.sort()
    #sayilar.sort(reverse=False)
    #Varsayılan değer False
    #Sayılar küçükten büyüğe sıralanır
    print(sayilar)
    
    sayilar.sort(reverse=True)
    #Sayılar büyükten küçüğe sıralanır
    print(sayilar)
    return sayilar
    
def kontrol():
    liste=sirala()
    sayi=int(input("Sayı:"))
    if sayi in liste:
        print("Tebrikler")
    else:
        print("Üzgünüz")

def kontrol2():
    liste=sirala()
    kullanici=[]
    sayac=0
    for i in range(1,6):
        while True:
            sayi=int(input("Sayı:"))
            if sayi>=1 and sayi<=10:
                break
        kullanici.append(sayi)
    print(kullanici)
    for i in kullanici:
        if i in liste:
            sayac+=1
    print(sayac)

def farklirastgele(x,y,miktar):
    liste=[]
    for i in range(miktar):
        while True:
            sayi=random.randint(x, y)
            if sayi in liste:
                pass
            else:
                break
        liste.append(sayi)
    print(liste)
farklirastgele(1, 10, 5)

rastgeleolustur()
rastgeleolustur2(50,100)
rastgeleolustur3(10,30,5)
sirala()
kontrol()
kontrol2()


