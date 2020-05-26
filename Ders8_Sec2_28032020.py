# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 15:02:23 2020

@author: Gözde Mihran Altınsoy
"""

#kendisine gönderilen bir sayıyı geri döndüren
def sayi(s):
    return s

print(sayi(5))

#lambda_adi=lambda parametre:dönen_deger(ler)
#parametre fonksiyona dışarıdan gönderilen değer(ler)

sayi2=lambda s:s

print(sayi2(5))

#kendisine gönderilen sayının 2 katını geri döndürsün
def kat2(sayi):
    return sayi*2

print(kat2(5))

kat=lambda sayi:sayi*2

print(kat(10))

#kendisine gönderilen değerin 10 fazlasını geri döndürsün
def fazla10(sayi):
    return sayi+10

print(fazla10(50))

fazla=lambda s:s+10

print(fazla(42))

#kendisine gelen 2 sayının toplamını geri döndüren
def toplam(x,y):
    return x+y

print(toplam(20,30))

topla=lambda x,y:x+y

print(topla(40,15))

#kendisine gönderilen iki sayının birbirine bölümünden kalanı hesaplatan fonksiyon
def kalan(bolunen,bolen):
    return bolunen%bolen

print(kalan(10,4))

k=lambda bolunen,bolen:bolunen%bolen

print(k(27,12))

#kendisine gönderilen iki sayının birbirine bölümünü int olarak geri döndüren fonksiyon
def bolum(bolunen,bolen):
    return int(bolunen/bolen)

print(bolum(30,12))

b=lambda bolunen,bolen:int(bolunen/bolen)

print(b(25,2))

#kendisine gönderilen listedeki en büyük değeri döndüren lambda
mak=lambda liste:max(liste)

liste=[20,4,6,25,7]
print(mak(liste))

#kendisine gönderilen metni tersten yazdıran lambda
ters=lambda kelime:kelime[::-1]

print(ters("Beykoz Üniversitesi"))


#kendisine gönderilen metnin 5. harfi ile 6. harfini geri döndüren lambda
metin=lambda kelime:kelime[4:6]

print(metin("Kocaeli"))

#kendisine gönderilen sayının tek veya çift olduğunu bulan lambda
tç=lambda sayi:sayi%2==0

if tç(10):
    print("Çifttir")
else:
    print("Tektir")

if tç(5):
    print("Çifttir")
else:
    print("Tektir")
    
tekcift=lambda sayi:"çift" if sayi%2==0 else "tek"

print(tekcift(10))
print(tekcift(5))

tekcift2=lambda sayi:print("Çifttir") if sayi%2==0 else print("Tektir")

tekcift2(20)
tekcift2(15)

#Kendisine gönderilen değer pozitifse 1, sıfıra eşitse 0, negatifse -1 değerini döndüren lambda
pozneg=lambda sayi:1 if sayi>0 else 0 if sayi==0 else -1 

print(pozneg(10))
print(pozneg(-10))
print(pozneg(0))

#Kendisine gönderilen değerin 2'ye,3'ye ve 6'e bölünme durumunu yazdırsın
bolunme=lambda sayi:print("6 bölünür") if sayi%6==0 else print("2 bölünür") if sayi%2==0 else print("3 bölünür") if sayi%3==0 else print("2,3,6 bölünmez")

bolunme(12)
bolunme(4)
bolunme(9)
bolunme(13)









