# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 10:49:48 2020

@author: Gözde Mihran Altınsoy
"""

"""
Txt Dosya Açma Kipleri ve Açıklamaları
'r' modu: Dosyayı sadece okumak için açar. Bu mod varsayılan moddur.
'r+' modu: Dosyayı hem okumak hem de yazmak için açar. Eğer çağrılan dosya bulunamadıysa yeni bir dosya oluşturulmaz.

#r ve r+ kipleri ile sadece dosya varsa açabiliriz eğer dosya yoksa hata verir.

'w' modu: Dosyayı sadece yazmak için açar. Varolan dosyanın üzerine yazma işlemini yapar. Eğer çağrılan dosya bulunamadıysa yeni bir dosya oluşturur.
'w+' modu: Dosyayı hem okumak hem de yazmak için açar. Varolan dosyanın üzerine yazma işlemini yapar. Eğer çağrılan dosya bulunamadıysa yeni bir dosya oluşturur.

#w ve w+ kipleri dosya varsa üzerine yazar, yoksa yeni dosya oluşturur.

'a' modu: Dosyayı ekleme işlemi için açar. Eğer çağrılan dosya bulunursa, en sonundan eklemeye devam eder. Eğer dosya yoksa sadece yazma işlemi yapacak yeni bir dosya oluşturur.
'a+' modu: Dosyayı hem ekleme hem de okuma işlemi için açar. Eğer çağrılan dosya bulunursa, en sonundan eklemeye devam eder. Eğer dosya yoksa yazma ve okuma işlemleri yapacak yeni bir dosya oluşturur.

#a ve a+ kipleri dosya yoksa oluşturur, varsa üzerine ekleme yapmamızı sağlar.
"""

#dosya = open('metin_dosyasi.txt', 'r') # r modunda dosyamızı açtık.
#Eğer dosya yoksa r modunda açamaz 
#FileNotFoundError: [Errno 2] No such file or directory: 'metin_dosyasi.txt'
#hatasını döndürür


dosya = open('metin_dosyasi.txt', 'w') # w modunda dosyamızı açtık.
dosya.write("merhaba")
dosya.close()




dosya = open('metin_dosyasi.txt', 'w+') # w+ modunda dosyamızı açtık.
dosya.write("merhaba\nöğrencilerim\n")

print(dosya.tell())
dosya.seek(0) #dosyanın başına gider (0.bit - başlangıç noktası)

print(dosya.read())

dosya.seek(0)
print(dosya.tell())
veri=dosya.readline() #kursörün bulunduğu satırı alır ve bir alt satıra geçer 
print(veri)
print(dosya.tell())

print(dosya.readline())
dosya.close()

print()

dosya = open('metin_dosyasi.txt', 'r')
veri=dosya.read()
print(veri)
dosya.close()


#dosya.write("deneme")  #dosya r kipiyle açıldığı için hata oluşur
#UnsupportedOperation: not writable


#dosya = open('deneme.txt', 'r+') #eğer deneme dosyası yoksa hata oluşur
#FileNotFoundError: [Errno 2] No such file or directory: 'deneme.txt'

print()




dosya = open('metin_dosyasi.txt', 'r+')
print(dosya.read())
dosya.write("Bugün hava bulutlu\n")

dosya.seek(0)
print(dosya.read())

dosya.close()




dosya = open('metin_dosyasi.txt', 'a')

dosya.write("Nasılsınız?\n")

dosya.write("Ben çok iyiyim\n")

#print(dosya.read()) #dosya okuma işlemi bu kipte yapılamaz. Hata oluşur
#UnsupportedOperation: not readable
dosya.close()



dosya = open('metin_dosyasi.txt', 'a+')

dosya.write("Nasılsınız?\n")

dosya.write("Ben çok iyiyim")

dosya.seek(0)

print(dosya.read()) 

dosya.close()


#split ile sayıların tam kısmı ile ondalıklarını ayıralım.
print()
a=["1.3","2.4"]
b=[]
c=[]
for i in a:
    b.append(int(i.split(".")[0])) #Bu değeri listeye eklerken int değere dönüştürdük
    c.append(int(i.split(".")[1])) #Bu değeri listeye eklerken int değere dönüştürdük
print("b:",b,"c:",c)    
print()

#Soru:
#Bir dosyayı sıfırdan oluşturup hem okuma hem de yazma modunda açalım
#açma Kipi : w+
#sayılar : 10 tane 1 ile 20 arasındaki random sayı tutacak
#Bu sayıları alt alta dosyaya yazdıralım
#Bu dosya içerisinde tek sayıları teksayilar isimli dosyaya, çift sayıları çift sayılar isimli dosyaya atayalım

with open("sayilar.txt","w+") as dosya:
    #Bu şekilde dosya açıldığında close ile kapatmaya gerek yoktur. Bu blok bittiğinde dosya otomatik kapanır
    from random import randint
    #dosya.write("3")
    for i in range(1,11):
        dosya.write(str(randint(1,20))+"\n")
    dosya.seek(0)
    
    print(dosya.read())
    
    veriler=[]
    dosya.seek(0)
    #veriler.append(dosya.read())
    #print(veriler)
    
    liste=[]
    liste.append(dosya.readline())
    liste.append(dosya.readline())
    liste.append(dosya.readline())
    print(liste) 
    
    
    
    
    
    dosya.seek(0)
    liste=[]
    liste=dosya.readlines()
    print(liste)
    
    
    
    sayilar=[]
    for i in liste:
        #5\n split -> '5' ''
        print(i.split("\n"))
        sayilar.append(int(i.split("\n")[0]))
        #dosyadan alınan değerler str türünde saklanır. Listeye eklerken int'e dönüştürdük
        #split ile iki tane değer elde ettik. Bu değerlerden biri sayı biri de boş bir karakter oldu
        #Bizim sayı değerini alabilmemiz için 0. indisteki sayının tutulduğu değere ihtiyacımız var. Bu yüzden split işleminden sonra0.indisi almak adına [0] indis değerini yazdık
    print(sayilar)
    
with open("teksayilar.txt","w+") as dosya:
    for sayi in sayilar:
        if sayi%2==1:
            dosya.write(str(sayi)+"\n")
    dosya.seek(0)
    print(dosya.readlines())
    
with open("ciftsayilar.txt","w+") as dosya:
    for sayi in sayilar:
        if sayi%2==0:
            dosya.write(str(sayi)+"\n")
    dosya.seek(0)
    print(dosya.readlines())    
     

#Bir öğrenci listemizin tutulduğu dosyamız var. Bu öğrenci listemizde AA, BB, BA, FF gibi öğrencilerimizin harf notları var
#Bu dosyadaki FF notuna sahip öğrencileri "kalanlar" isimli dosyaya, diğer öğrencileri "geçenler" isimli dosyaya yazdıralım
#Dosyalara sadece isim soyisimler atılacak
#Örn Dosyamız:
"""
Ayşe Kaya,AA
Ali Aykut Eren,FF
Kemal Uçak,BB
Şule Kule,CC
Pelin Akın,FF
"""
with open("öğrenciler.txt","w+") as dosya:
    dosya.write("Ayşe Kaya,AA\nAli Aykut Eren,FF\nKemal Uçak,BB\nŞule Kule,CC\nPelin Akın,FF\n")  
    dosya.seek(0)
    liste=dosya.readlines()
    
isimler=[]
notlar=[]    
print(liste)
for deger in liste:
    isimler.append(deger.split(",")[0])
    n=deger.split(",")[1]
    notlar.append(n.split("\n")[0])
print("isimler:",isimler,"notlar",notlar)

with open("geçenler.txt","w+") as dosya:
    for i in range(len(notlar)):
        if notlar[i]!="FF":
            dosya.write(isimler[i]+"\n")
    dosya.seek(0)
    print(dosya.readlines())
    
with open("kalanlar.txt","w+") as dosya:
    for i in range(len(notlar)):
        if notlar[i]=="FF":
            dosya.write(isimler[i]+"\n")
    dosya.seek(0)
    print(dosya.readlines())












