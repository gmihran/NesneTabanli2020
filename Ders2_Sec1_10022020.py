# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 10:15:32 2020

@author: gozdemihranaltinsoy
"""

# Girilen sayıyı tersten yazdıralım
#1.yöntem:
sayi=input("Sayı:") #Kullanıcıdan string veri tipinde bir değer aldık
print(sayi[::-1])

# Girilen sayıyı tersten yazdıralım
#2.yöntem:
sayi=int(input("Sayı:")) #Kullanıcıdan integer veri tipinde bir değer aldık
strsayi=str(sayi) #Değeri string veri türüne dönüştürdük
print(strsayi[::-1]) #string değer ile string parçalama işlemi yapılabilir

# Girilen sayıyı tersten yazdıralım
#3.yöntem:
sayi=int(input("Sayı:")) #Kullanıcıdan integer veri tipinde bir değer aldık
sayi2=sayi #sayının içeriğini değiştirmemek adına kopyasını aldık
while(sayi2>=10):
    print(sayi2%10,end="") 
    #print içerisine yazılan end="" kodu alt satıra geçmeden yazma işleminin sürdürülmesini sağlar
    sayi2=int(sayi2/10)
print(sayi2)

# Girilen sayıyı tersten yazdıralım
#4.yöntem:
sayi=int(input("Sayı:")) #Kullanıcıdan integer veri tipinde bir değer aldık
sayi2=sayi #sayının içeriğini değiştirmemek adına kopyasını aldık
ters=0
while(sayi2>=1):
    ters=ters*10+sayi2%10
    sayi2=sayi2//10 #bölüm işleminde sadece tam kısmını almamızı sağlar, ondalık kısmını atıyoruz 
print(ters)
  
#String bir ifadedeki tüm harflerin arasına virgül koyarak yan yana ekrana yazdıralım
kelime="Beykoz Üniversitesi"
for harf in kelime:
    print(harf,end=",") #end="," kodunu kullanmazsak tüm harfleri alt alta yazdırırız
 
#Kelimenin içerisinde sadece "e" harflerini yazdıralım     
print()
kelime="Beykoz Üniversitesi"
for harf in kelime:
    if harf=="e": #karşılaştırma işlemlerinde iki eşittir (==) kullanılır
#atama işlemlerinde tek eşittir (=) kullanılır
        print(harf)

#String bir ifadedeki tüm harfleri birer atlayarak ekrana yazdıralım
kelime="Beykoz Üniversitesi"
#Byo nvriei
print(kelime[::2])


# Girilen sayının tam sayı olup olmadığını yazdıralım
sayi=eval(input("Sayı:"))
#eval klavyeden girilen değer tam sayı ise int, ondalıklı sayı ise float değişkende saklanmasını sağlar
print(type(sayi))
if type(sayi)==int:
    #Ör: 12 
    print("Tam sayı")
elif type(sayi)==float:
    #Ör: 12.4
    print("Ondalıklı sayı")
else:
    #Ör: 12,4,2,5 değerleri girildiğinde:
    print("Tuple (Liste)")

#Eğer girilen değer int ise kaç rakamdan oluştuğunu yazdıralım
if type(sayi)==int:
    print(len(str(sayi)))

#Eğer girilen değer int ise aşağıdaki işlemleri yaptıralım
#Rakamların sayısı 1-10 A
#Rakamların sayısı 10-20 B
#Rakamların sayısı 20 üzeri C
if type(sayi)==int:
    uzunluk=len(str(sayi))
    if uzunluk<=10:
        print("A")
    elif uzunluk<=20:
        print("B")
    else:
        print("C")


#1'den 100'e kadar olan sayıları yan yana araya boşluk koyarak ekrana yazdıralım
print("\n1-100 Arasındaki tüm sayılar:")
for i in range(1,101):
    #range(başlangıç değeri, bitiş değeri+1,artış miktarı)
    #Artış değeri 1 ise yazmaya gerek yok
    print(i,end=" ")

#1'den 100'e kadar olan sayılardan tek olanları yan yana araya boşluk koyarak ekrana yazdıralım
print("\n1-100 Arasındaki tüm tek sayılar:")
for i in range(1,101):
    if i%2==1:
        print(i,end=" ") 

#1'den 100'e kadar olan sayılardan tek olanları yan yana araya boşluk koyarak ekrana yazdıralım
print("\n1-100 Arasındaki tüm tek sayılar:")
for i in range(1,101,2):
    print(i,end=" ") 


#Girilen 2 sayının birbirine tam bölünüp bölünmediğini veren program
#sayi1=11
#sayi2=5
sayi1=int(input("1.sayı:"))
sayi2=int(input("2.sayı:"))
#1.yöntem:
if sayi1%sayi2==0:
    print("tam bölünür")
else:
    print("tam bölünmez")

#2.yöntem:
if sayi1/sayi2==sayi1//sayi2:
    print("tam bölünür")
else:
    print("tam bölünmez")

#3.yöntem: 
if sayi1/sayi2==int(sayi1/sayi2):
    print("tam bölünür")
else:
    print("tam bölünmez")


#Girilen bir sayının tam bölenlerini ekrana yazdıran program
#10 sayısının tam bölenleri: 1,2,5,10
#33 sayısının tam bölenleri: 1,3,11,33
#29 sayısının tam bölenleri: 1,29
sayi=int(input("Sayı:"))

#boş bir liste (list) oluşturalım:
#1.yöntem:
liste=[] #boş bir liste oluşturuldu
#2.yöntem:
liste=list() #boş bir liste oluşturuldu
for bolen in range(1,sayi+1):
    #range ifadesindeki son değerde son değerin 1 fazlasını yazmalıyız
    #Ör: son değer; sayi ise sayi+1 yazmalıyız
    if sayi%bolen==0:
        #sayi bolen değerine tam bölünüyorsa;
        liste.append(bolen)
        #bolen değeri listeye eklendi
print(liste)
print(type(liste))

#list (liste) değişken türüne veri eklemek için append fonksiyonu kullanılır

#tuple oluşturalım
#tuple değiştirilemeyen listelerdir
#okunabilir ama üzerinde değişiklik yapılamayan listelerdir
sayilar=(1,2,3)
print(sayilar)
print(type(sayilar))

#liste oluşturalım
#hem okunabilir, hem de üzerine yazılabilir listelerdir
liste=[1,2,3]
liste.append(4)
print(liste)
print(type(liste))


#Bir sayının mükemmel sayı olup olmadığını bulan program
#Mükemmel sayı: Kendisi dışında kendisine tam bölünen sayıların toplamı kendisine eşit olan sayılar
#Mükemmel sayı ör: 6, 28, 496, 8128
sayi=int(input("Sayı:"))
bolenler=[]
for bolen in range(1,sayi):
    if sayi%bolen==0:
        bolenler.append(bolen)
if sum(bolenler)==sayi:
    print("Mükemmel sayıdır")
else:
    print("Mükemmel sayı değildir")

#Haftaya buradan devam edeceğiz...

#Çalışma ödevi: 1 ile 10000 arasındaki mükemmel sayıları ekrana yazdıralım

#Kullanıcıdan alınan 4 kenar bilgisine göre şeklin dikdörtgen, kare veya diğer dörtgen olduğunu söylesin

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
