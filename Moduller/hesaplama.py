# -*- coding: utf-8 -*-
"""
Created on Mon Mar  9 15:14:18 2020

@author: gozdemihranaltinsoy
"""
PI=3

#Kendisine gönderilen iki sayının toplamını hesaplayan metod:
def topla(s1,s2):
    return s1+s2

#Kendisine gönderilen iki sayının farkını hesaplayan metod:
def cikar(s1,s2):
    return s1-s2

#Kendisine gönderilen iki sayının çarpımını hesaplayan metod:
def carp(s1,s2):
    return s1*s2

#Kendisine gönderilen iki sayının bölümünü hesaplayan metod:
def bol(s1,s2):
    try:
        return s1/s2
    except ZeroDivisionError:
        return "Sıfıra bölme hatası oluştu"
    except:
        return "Tanımsız değer"




