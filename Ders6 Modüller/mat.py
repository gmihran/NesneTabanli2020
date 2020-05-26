# -*- coding: utf-8 -*-
"""
Created on Mon Mar  9 15:34:47 2020

@author: gozdemihranaltinsoy
"""

#Kendisine gönderilen sayının faktöriyelini hesaplayan ve sonucu geri döndüren metod:
def faktoriyel(sayi):
    #5!=1*2*3*4*5=120
    #0!=1
    #-5!=Tanımsız
    sonuc=1
    if sayi<0:
        return "Tanımsız"
    for i in range(1,sayi+1):
        sonuc*=i #sonuc=sonuc*i
    return sonuc


#Sayının karesini ekrana yazdıran metod:
def kare():
    sayi=int(input("Sayı:"))
    print(sayi*sayi)


#Kendisine gönderilen sayı ve üs değerlerine göre üssünü hesaplayıp
#ekrana yazdıran metod:
def kuvvet(sayi,us):
    return sayi**us

#Rastgele 1 ile 100 arasında üretilen 10 sayıyı ekrana yazdırıp, toplamlarını döndüren (return) metod:
def rastgele():
    import random
    sayilar=[]
    for i in range(1,11):
        sayilar.append(random.randint(1,100))
    print(sayilar)
    return sum(sayilar)

#Klavyeden girilen iki sayının birbirine bölümünden kalanı ekrana yazdıran metod:
def mod():
    bolunen=eval(input("Bölünen:"))
    bolen=eval(input("Bölen:"))
    print("Kalan=",bolunen%bolen)
    
#Kendisine gönderilen değer kadar kendisine gönderilen
#min ve mak değerler arasında random değer üretip
#bu değerleri ana metoda döndüren metod:
#Parametre 3 değer, döndürülen random değerler (liste)
#ÖR/ 5,1,100 5 tane 1 ile 100 arasında değer üretip bu değerler ekrana yazdırılacak
    
def sayi_uret(miktar,bas,bit):
    import random
    sayilar=[]
    for i in range(miktar):
        sayilar.append(random.randint(bas,bit))
    return sayilar
    
    
    
    
    
    
    
    
    
    
    
    
    