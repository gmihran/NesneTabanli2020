# -*- coding: utf-8 -*-
"""
Created on Mon Mar  9 10:16:57 2020

@author: gozdemihranaltinsoy
"""

#%%
#Çalışma Sorusu:
#Çarpım tablosu
#aralarda tab boşluğu var
#1*1=1    2*1=2    3*1=3    4*1=4    5*1=5
#1*2=2    2*2=4......................5*2=10
#..........................................
#1*10=10 2*10=20   3*10=30  4*10=40  5*10=50    
#%%

for i in range(1,11):
    for j in range(1,6):
        print(j,"*",i,"=",i*j,end="\t")
    print()

#%%
#Modüller 
#(Metodlar - Fonksiyonlar)

#Kendisine gönderilen iki sayının toplamını hesaplayan metod:
#%%
import islemler
print(islemler.topla(5,2))
sonuc=islemler.topla(10,3)
print(sonuc)
print(islemler.bol(10,3))
print(islemler.bol(10,0))
print(islemler.cikar(10,3))
print(islemler.carp(10,3))

#%%
from islemler import topla,cikar,carp
print(topla(4,5))
print(cikar(4,5))
print(carp(4,5))
#print(bol(3,2)) #Hata

#%%
from islemler import *
print(PI)
print(bol(5,2))


#%%
import islemler as islem
print(islem.topla(3,4))
print(islemler.topla(3,4))

#%%
#Kendisine gönderilen sayının faktöriyelini hesaplayan metod:
#%%
import matematik 
print(matematik.faktoriyel(5))
print(matematik.faktoriyel(10))
print(matematik.faktoriyel(0))
print(matematik.faktoriyel(-5))
#%%
#Sayının karesini ekrana yazdıran metod:
#%%
import matematik
print(matematik.kare("a"))
print(matematik.kare(4))
print(matematik.kare2("a"))
print(matematik.kare2("4"))

#%%
#Kendisine gönderilen sayı ve üs değerlerine göre üssünü hesaplayıp
#ekrana yazdıran metod:
#%%
import matematik
print(matematik.us(2,3))
print(matematik.us(2,"a"))
print(matematik.us("a","a"))
print(matematik.us(5,4))
#%%
#Rastgele 1 ile 100 arasında üretilen 10 sayıyı ekrana yazdırıp, toplamlarını döndüren (return) metod:
#%%
import matematik
print("Toplam:",matematik.rastgele())
#%%
#Klavyeden girilen iki sayının birbirine bölümünden kalanı ekrana yazdıran metod:
#%%
import matematik as mat
mat.mod()

#%%
#Kendisine gönderilen değer kadar kendisine gönderilen
#min ve mak değerler arasında random değer üretip
#bu değerleri ana metoda döndüren metod:
#Parametre 3 değer, döndürülen random değerler (liste)
#%%
import matematik
print(matematik.sayi_uret(5,10,25))
print(matematik.sayi_uret(5,25,10))
print(matematik.sayi_uret(5,25,25))
print(matematik.sayi_uret(-5,10,25))
#%%
#XOX oyunu
#Bir kullanıcı, bir bilgisayar arasında oyun oynanacak
#Sırayla X ve O değerleri matrise yazılacak
liste=[0,1,2,3,4,5,6,7,8]
while True:
    secim=input("Seçiminiz X/O:")
    if secim=="X" or secim=="O":
        break
if secim=="X" :
    pcsecim="O"
else:
    pcsecim="X"

def yazdir():
    sayac=0
    for i in range(3):
        for j in range(3):
            print(liste[sayac],end="\t")
            sayac+=1
        print()
        
def kullanici():
    kontrol=True
    while True:
        tercih=int(input("Tercihiniz:"))
        for i in range(9):
            if liste[i]==tercih:
                liste[i]=secim
                kontrol=False
        if kontrol==False:
            break
        
def bilgisayar():
    #bilgisayar mantıklı bir seçim yapmıyor
    #rastgele bir seçim yapıyor
    #bu seçim iyileştirilmelidir
    import random
    while True:
        rand=random.randint(0,8)
        if liste[rand]!="X" and liste[rand]!="O":
            break
    liste[rand]=pcsecim
def kontrol():
    pass
    #Bir XOX, OOO veya XXX yazdı mı?
    #Oyun bitti mi?
    #Kim kazandı, berabere mi?

#Aşağıdaki fonksiyonlar oyun bitene kadar sürekli çağrılacak
yazdir()
kullanici()
bilgisayar()


#%%
"""
tuple (demet) ()
list (liste) []
dict (sözlük) {}
"""
#Liste ile Demet arasındaki fark nedir?
#eval ile int float arasındaki fark nedir?
#String parçalama
#Kod soruları (for, while, if...)
#Fonksiyonlar (metodlar)
#Girilen 10 sayıdan tek sayıları listeye atayıp listeyi ekrana yazdırınız.


