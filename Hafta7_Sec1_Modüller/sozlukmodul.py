# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 12:04:55 2020

@author: Gözde Mihran Altınsoy

Bu modülde sözlük işlemlerini uygularız
"""

sozluk={"isim":"Gözde","soyisim":"Altınsoy","unvan":"Öğretim Görevlisi"}

def sozlukislem():
    print(sozluk["isim"])
    
    sozluk["yaş"]=33
    
    print(sozluk["yaş"])
    
    print(sozluk)
    
    print(sozluk.keys())
    
    print(sozluk.values())

