# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 16:02:42 2020

@author: Gözde Mihran Altınsoy

Bu modül mevsimler ile ilgili işlemleri içermektedir
"""


mevsim=["ilkbahar","yaz","sonbahar","kış"]

def yazdir():
    print(mevsim)
    
def ilkmevsim():
    print(mevsim[0])
    
def ilkmevsimgetir():
    return mevsim[0]

def mevsimsayisi():
    print(len(mevsim))

def mevsimsayisigetir():
    return len(mevsim)

yazdir()
mevsimsayisi()