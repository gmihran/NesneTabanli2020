# -*- coding: utf-8 -*-
"""
Created on Mon Mar  9 15:02:45 2020

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
        #end="" yan yana yazmamızı,
        #end="\t" ise yan yana yazdırırken aralarına tab boşluğu bırakmamızı sağladı
    print()
    
#%%
#Modüller 
#(Metodlar - Fonksiyonlar)

#Kendisine gönderilen iki sayının toplamını hesaplayan metod:
#%%
import hesaplama
#modülün adını yazarak içerisindeki tüm yapılara ulaşabiliriz
print(hesaplama.topla(5,3))
print(hesaplama.cikar(10,15))
print(hesaplama.carp(10,15))
print(hesaplama.bol(10,15))
print(hesaplama.bol(10,0)) #Sıfıra bölme hatası oluştu
print(hesaplama.bol(10,"a")) #Tanımsız değer
print(hesaplama.bol("a","a")) #Tanımsız değer
print(hesaplama.PI) #3

#%%
from hesaplama import topla,cikar
#modülün içerisindeki topla,cikar metodlarını projemize dahil eder. Modülün adını yazmamıza gerek kalmaz
print(topla(2,3))
print(cikar(3,4))
#%%
from hesaplama import *
#modülün içerisindeki tüm fonksiyon ve yapıları projemize dahil eder. Modülün adını yazmamıza gerek kalmaz
print(topla(2,4))
print(bol(4,5))

#%%
import hesaplama as hesap
#hesaplama modülüne hesap adıyla ulaşabilmemizi sağlar. hesaplama adını kullanmaya da devam edebiliriz
print(hesap.topla(3,4))
print(hesaplama.topla(3,4))
#%%
#Kendisine gönderilen sayının faktöriyelini hesaplayan metod:
#%%
import mat
print(mat.faktoriyel(5))
print(mat.faktoriyel(2))

#%%
#Sayının karesini ekrana yazdıran metod:
#%%
import mat
print(mat.kare())

#%%
#Kendisine gönderilen sayı ve üs değerlerine göre üssünü hesaplayıp
#ekrana yazdıran metod:
#%%
import mat
print(mat.kuvvet(4,5))
print(mat.kuvvet(4,-2))

#%%
#Rastgele 1 ile 100 arasında üretilen 10 sayıyı ekrana yazdırıp, toplamlarını döndüren (return) metod:
#%%
import mat
print("Toplam:",mat.rastgele())

#%%
#Klavyeden girilen iki sayının birbirine bölümünden kalanı ekrana yazdıran metod:
#%%
import mat
mat.mod()

#%%
#Kendisine gönderilen değer kadar kendisine gönderilen
#min ve mak değerler arasında random değer üretip
#bu değerleri ana metoda döndüren metod:
#Parametre 3 değer, döndürülen random değerler (liste)
#%%
import mat
print(mat.sayi_uret(5,20,50))
print(mat.sayi_uret(12,15,150))
sayilar=mat.sayi_uret(10,3,150)
print(sayilar)
print("Maksimum:",max(sayilar))
print("Minimum:",min(sayilar))
print("Toplamları:",sum(sayilar))
print("Miktarı:",len(sayilar))
print("Ortalaması:",sum(sayilar)/len(sayilar))
#%%
#XOX oyunu
#Bir kullanıcı, bir bilgisayar arasında oyun oynanacak
#Sırayla X ve O değerleri matrise yazılacak
while True:
    secim=input("Seçiminiz X/O:")
    if secim=="X" or secim=="O":
        break
if secim=="X":
    pcsecim="O"
else:
    pcsecim="X"

liste=[1,2,3,4,5,6,7,8,9]
def yazdir():
    sayac=0
    for i in range(0,9):
        if sayac==3:
            print()
            sayac=0
        print(liste[i],end="\t")
        sayac+=1
        
def kullanici():
    kontrol=True
    while True:
        tercih=int(input("Tercih:"))
        for i in range(0,9):
            if tercih==liste[i]:
                liste[i]=secim
                kontrol=False
                break
        if kontrol==False:
            break
        
def bilgisayar():
    #bilgisayar mantıklı bir seçim yapmıyor
    #rastgele bir seçim yapıyor
    #bu seçim iyileştirilmelidir
    import random
    while True:
        pctercih=random.randint(0,8)
        if liste[pctercih]!="X" and liste[pctercih]!="O":
            break
    liste[pctercih]=pcsecim
    
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
"""
1.başla
2.teksayilar=[]
3.Döngü başlat i (10)
4.Oku sayi
5.Eğer sayi%2=1 ise teksayilar.append(sayi)
6.Döngü bitir
7.Yaz teksayilar
8.Bitir
"""
