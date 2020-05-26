# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 11:48:59 2020

@author: Gözde Mihran Altınsoy

Bu modülde string parçalama işlemleri yapıyoruz
"""

kelime="Beykoz Üniversitesi"
def ilkkelime():
    print(kelime[0:6])
    
    
kelime="Bugün hava güzel"
def ilkkelime2():
    yenikelime=""
    for harf in kelime:
        if harf==" ":
            break
        print(harf,end="")
        yenikelime=yenikelime+harf
    print("\n",yenikelime)
    
kelime="Beykoz Üniversitesi"
def terskelime():
    print(kelime[::-1])
    
def ilkharf():
    print(kelime[0])

def sonharf():
    print(kelime[-1])

def kaydir():
    print(kelime[:6:2])
    #Başlangıç değeri belirtilmez ise 0'dan başlar
    
def kaydir2():
    print(kelime[::2])
    #Başlangıç ve bitiş değeri belirtilmez ise 0'dan başlar
    #Kelimenin sonuna kadar gider
    
ilkkelime()
ilkkelime2()
terskelime()
ilkharf()
sonharf()
kaydir()
kaydir2()