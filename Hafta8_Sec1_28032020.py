# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 09:59:14 2020

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

kare=lambda sayi:sayi*2

print(kare(10))

#kendisine gönderilen değerin 10 fazlasını geri döndürsün
def fazla10(sayi):
    return sayi+10

print(fazla10(25))

f=lambda sayi:sayi+10
print(f(30))

#kendisine gelen 2 sayının toplamını geri döndüren
def toplam(x,y):
    return x+y

print(toplam(5,7))

t=lambda x,y:x+y

print(t(4,6))

#kendisine gönderilen iki sayının birbirine bölümünden kalanı hesaplatan fonksiyon
def kalan(bolunen,bolen):
    return bolunen%bolen

print(kalan(10,6))

k=lambda bolunen,bolen:bolunen%bolen

print(k(6,4))

#kendisine gönderilen iki sayının birbirine bölümünü int olarak geri döndüren fonksiyon
def bolum(bolunen,bolen):
    return int(bolunen/bolen)

print(bolum(10,4))

b=lambda bolunen,bolen:int(bolunen/bolen)

print(b(20,6))

#kendisine gönderilen listedeki en büyük değeri döndüren lambda
mak=lambda liste:max(liste)

sayilar=[1,2,10,25,12,4]
print(mak(sayilar))

#kendisine gönderilen metni tersten yazdıran lambda
ters=lambda metin:metin[::-1]

print(ters("Beykoz Üniversitesi"))


#kendisine gönderilen metnin 5. harfi ile 6. harfini geri döndüren lambda
harf=lambda metin:metin[4:6]

print(harf("Kocaeli"))

#kendisine gönderilen sayının tek veya çift olduğunu bulan lambda
tekcift=lambda sayi:sayi%2==0

print(tekcift(10))
if tekcift(10):
    print("Çifttir")
else:
    print("tektir")
    
print(tekcift(5))
if tekcift(5):
    print("çifttir")
else:
    print("tektir")

tekcift2=lambda sayi:"çifttir" if sayi%2==0 else "tektir"

print(tekcift2(10))
print(tekcift2(5))

tekcift2=lambda sayi:print("çifttir") if sayi%2==0 else print("tektir")

tekcift2(10)
tekcift2(5)

tekcift3=lambda sayi:print(sayi," çifttir") if sayi%2==0 else print(sayi," tektir")

tekcift3(10)
tekcift3(5)

#Kendisine gönderilen değer pozitifse 1, sıfıra eşitse 0, negatifse -1 değerini döndüren lambda
f = lambda x: 1 if x>0 else 0 if x ==0 else -1

print(f(5))
print(f(-5))
print(f(0))


#Kendisine gönderilen değerin 2'ye,3'ye ve 6'e bölünme durumunu yazdırsın
a=lambda sayi:print(sayi," 6 bölünür") if sayi%6==0 else print(sayi," 2 bölünür") if sayi%2==0 else print(sayi," 3 bölünür") if sayi%3==0 else print(sayi," 2,3,6 bölünmez") 
                                                                                                                                #bu şekilde detaylı if else içeren bir örnek sınavda sorulmayacaktır

a(12)
a(10)
a(9)
a(13)
