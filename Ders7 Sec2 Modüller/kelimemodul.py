# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 16:14:06 2020

@author: Gözde Mihran Altınsoy

Bu modülde string parçalama işlemleri yapılmaktadır.
"""

kelime="MYO Beykoz Üniversitesi"

def ilkkelime():
    print(kelime[0:6])

ilkkelime()

kelime="bugünlerde hava güzel"
def ilkkelime2():
    yenikelime=""
    for harf in kelime:
        if harf==" ":
            break
        print(harf,end="")
        yenikelime+=harf
    print("\n",yenikelime)
        
        
ilkkelime2()

def ilkharf():
    print(kelime[0])
    
ilkharf()

def sonharf():
    print(kelime[-1])    
    
sonharf()  

kelime="Beykoz Üniversitesi MYO"
def kaydir():
    print(kelime[:6:2])
    
kaydir()    
    
def kaydir2():
    print(kelime[::2])    
    
kaydir2()


def tersyazdir():
    print(kelime[::-1])

tersyazdir()



