# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 10:33:46 2020

@author: Gözde Mihran Altınsoy

Bu modül ile mevsimler üzerinde çalışmalar yapılacaktır

"""

mevsimler=["ilkbahar","yaz","sonbahar","kış"]

def ilkmevsim():
    print(mevsimler[0])

def ilkmevsimgetir():
    return mevsimler[0]

def mevsimsayisi():
    print(len(mevsimler))
    
def mevsimsayisigetir():
    return len(mevsimler)

"""   
ilkmevsim()

print(ilkmevsimgetir())
mevsim=ilkmevsimgetir()
print(mevsim)
"""