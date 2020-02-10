# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 15:07:13 2020

@author: gozdemihranaltinsoy
"""
"""
# Girilen sayıyı tersten yazdıralım
sayi=input("Sayı:")
print(sayi[::-1])

# Girilen sayıyı tersten yazdıralım
sayi1=int(input("Sayı:"))
print(str(sayi1)[::-1])

# Girilen sayıyı tersten yazdıralım
sayi1=int(input("Sayı:"))
sayi2=sayi1 #sayının yedeğini aldık
#sayının üzerinde işlem yaptığımız için sayının ilk değeri kaybolur, bu yüzden yedeğini alıyoruz
ters=0
while sayi2>=1:
    ters=ters*10+sayi2%10
    sayi2=sayi2//10 #bölüm sonucunun tam kısmını alır, ondalık kısmını atar
    #sayi2=int(sayi2/10)
print(sayi1," sayısının tersi: ",ters)

# Girilen sayının tam sayı olup olmadığını yazdıralım
sayi=eval(input("Sayı:"))

#1.yöntem:
print(type(sayi))
if type(sayi)==int:
    print("Tam sayıdır")
elif type(sayi)==float:
    print("Ondalıklı sayıdır")
else:
    print("Tuple (demet) türündedir")

#2.yöntem:
if int(sayi)==sayi:
    print("Tam sayıdır")
else:
    print("Ondalıklı sayıdır")

#String bir ifadedeki tüm harflerini alt alta yazdıralım
kelime="Beykoz Üniversitesi"
for harf in kelime:
    print(harf)

#String bir ifadedeki tüm harflerin arasına virgül koyarak yan yana ekrana yazdıralım
kelime="Beykoz Üniversitesi"
for harf in kelime:
    print(harf,end=",") #print içerisine yazılan end="," kodu alt satıra geçmeden yazma işleminin araya virgül koyarak sürdürülmesini sağlar
print()
#Kelimenin içerisinde sadece "e" harflerini yazdıralım     
kelime="Beykoz Üniversitesi"
for harf in kelime:
    if harf=="e": #karşılaştırma işlemlerinde iki eşittir (==) kullanılır
#atama işlemlerinde tek eşittir (=) kullanılır
        print(harf) 
    
#String bir ifadedeki tüm harfleri birer atlayarak ekrana yazdıralım
kelime="Beykoz Üniversitesi"
#Byo nvriei
print(kelime[::2])

#1'den 100'e kadar olan sayıları ekrana yazdıralım
for i in range(1,101):
    #range(başlangıç değeri,bitiş değeri+1,artış/azalış miktarı)
    #Eğer artış/azalış miktarı belirtilmemişse değer 1 olarak kabul edilir
    print(i,end=" ")
print()

#100'den 5'e kadar olan sayıları ekrana yazdıralım
for i in range(100,4,-1):
    #range(başlangıç değeri,bitiş değeri+1,artış/azalış miktarı)
    #Eğer artış/azalış miktarı belirtilmemişse değer 1 olarak kabul edilir
    print(i,end=" ")

#1'den 100'e kadar olan sayılardan tek olanları ekrana yazdıralım
#1.yöntem:
for i in range(1,101,2):
    print(i)

#2.yöntem:
for i in range(1,101):
    if i%2==1:
        print(i)
    
#Girilen 2 sayının birbirine bölünüp bölünmediğini veren program:
#1.yöntem:
sayi1=int(input("1.sayı:"))
sayi2=int(input("2.sayı:"))
print(sayi1/sayi2)
if sayi1%sayi2==0:
    print("Tam bölünür")
else:
    print("Tam bölünmez")

#2.yöntem:
if sayi1/sayi2==sayi1//sayi2:
    print("Tam bölünür")
else:
    print("Tam bölünmez")

#Girilen bir sayının tam bölenlerini ekrana yazdıran program
#10= 1,2,5,10
#15= 1,3,5,15
#7=  1,7
sayi=int(input("Sayı:"))
for i in range(1,sayi+1):
    if sayi%i==0:
        print(i)

#Girilen bir sayının tam bölenlerini listeye atarak listeyi ekrana yazdıralım
sayi=int(input("Sayı:"))
liste=[]
#liste adında boş bir liste oluşturuldu
liste=list()
#liste adında boş bir liste oluşturuldu
print(type(liste))
for i in range(1,sayi+1):
    if sayi%i==0:
        liste.append(i)
print(liste)
print("Bölen sayısı:",len(liste))

#tuple oluşturalım
#tuple değiştirilemeyen listelerdir
#okunabilir ama üzerinde değişiklik yapılamayan listelerdir
mevsimler=("ilkbahar","yaz","sonbahar","kış")
print(mevsimler)
print(mevsimler[0])
#mevsimler[0]="yaz" #yapılamaz
        
#liste oluşturalım
#hem okunabilir, hem de üzerine yazılabilir listelerdir
mevsimler=["ilkbahar","yaz","sonbahar","kış"]
mevsimler[0]="yaz"
print(mevsimler)
print(mevsimler[0])
mevsimler.pop() # listedeki son elemanı siler
mevsimler.pop(2) # 2.indisi siler (sonbahar değerini sildi)
print(mevsimler)
"""

#Bir sayının mükemmel sayı olup olmadığını bulan program
#Mükemmel sayı: Kendisi dışında kendisine tam bölünen sayıların toplamı kendisine eşit olan sayılar
#Mükemmel sayı ör: 6, 28, 496, 8128
#6 => 1+2+3=6 Mükemmel sayı
#10 => 1+2+5=8 Mükemmel sayı değil
#28 => 1+2+4+7+14=28 Mükemmel sayı
sayi=int(input("Sayı:"))
bolenler=[]
for bolen in range(1,sayi):
    if sayi%bolen==0:
        bolenler.append(bolen)
if sum(bolenler)==sayi:
    print("Mükemmel sayıdır")
else:
    print("Mükemmel sayı değildir")

#Eğer girilen değer int ise aşağıdaki işlemleri yaptıralım
#Rakamların sayısı 1-10 A
#Rakamların sayısı 10-20 B
#Rakamların sayısı 20 üzeri C
sayi=eval(input("Sayı:"))
uzunluk=len(str(sayi))
print(uzunluk)
if type(sayi)==int:
    if uzunluk<=10:
        print("A")
    elif uzunluk<=20:
        print("B")
    else:
        print("C")


#Haftaya buradan devam edeceğiz...

#Çalışma ödevi: 1 ile 10000 arasındaki mükemmel sayıları ekrana yazdıralım

#Kullanıcıdan alınan 4 kenar bilgisine göre şeklin 
#dikdörtgen, kare veya diğer dörtgen olduğunu söylesin

#Çarpım tablosu
"""
    1*1=1
    1*2=2
    1*3=3
    ...
    1*10=10
    2*1=2
    2*2=4
    ...
    ...
    10*10=100
"""

#Girilen ismin harflerini alt alta yazdıran program
"""
isim="Beykoz"
büyükharf=isim.upper()
küçükharf=isim.lower()
ilkharfibüyük=isim.capitalize()
tersinedönüştür=isim.swapcase()
kelimeilkharfbüyüt=isim.title()
print(isim.islower())
#isim değişkeni küçük harflerden mi oluşuyor
print(isim.isupper())
#isim değişkeni büyük harflerden mi oluşuyor
print(isim.istitle())
#isim değişkendeki kelimelerin ilk harfleri
#büyük harflerden mi oluşuyor
print(isim.isspace())
#isim değişkeni boşluklardan mı oluşuyor kontrolü
print(isim)
print(isim.find("a"))
#verilen karakterin kaçıncı karakterde olduğunu verir
#sadece ilk bulduğunun indisini döndürür
#olmadığı takdirde -1 döndürür
print(isim.replace("a","e"))
#isim değişkeninde a değerinin yerine e değerini getirir
print(isim.replace("a",""))
#isim değişkeninde a değerinin yerine boş karakter getirir
#dolaylı yoldan silmiş oluruz
print(isim.rfind("a"))
#aramaya son karakterden başlar
#sağdan sola doğru arama yapar
print("*".join(isim))
#her harften sonra boşluk karakteri ekler
print(len(isim))
#isim değişkenin tuttuğu değerin karakter sayısını verir
"""
#Girilen bir kelimede tüm "a" harflerinin kaçıncı karakter olduğunu veren program

#Kelimenin Palindrom olup olmadığını bulan program
#kelimenin tersten okunuşu kendisiyle aynı mı?
#ör kayak, ey edip adanada pide ye, kek