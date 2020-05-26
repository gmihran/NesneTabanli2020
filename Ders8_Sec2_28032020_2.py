# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 15:40:54 2020

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

dosya=open("metin_dosyasi.txt","w")
dosya.write("merhaba\n")
dosya.write("nasılsınız?\n")
dosya.close()

dosya=open("metin_dosyasi.txt","w")
dosya.write("bugün hava kapalı\n")
dosya.write("??\n")
#print(dosya.read()) #Dosya w kipiyle açıldığında kesinlikle read ile okuma işlemi yapılamaz
#UnsupportedOperation: not readable hatası oluşur
dosya.close()

dosya=open("metin_dosyasi.txt","w+")
dosya.write("merhaba\n")
dosya.write("nasılsınız?\n")
print(dosya.tell()) #Kursörün bulunduğu noktayı bit türünden verir
dosya.seek(0) #0.bit değerine gitsin. Dosyanın başına (ilk noktasına) gittik
print(dosya.tell())
print(dosya.read()) #write ve read işlemlerinden sonra kursör dosyanın sonuna gider. Bu yüzden okuma işlemi yapmadan önce kursörü dosyanın ilk noktasına yönlendirmeliyiz
dosya.close()

dosya=open("metin_dosyasi.txt","r")
print(dosya.read())
#dosya.write("İyiyim") #r kipiyle açılan dosyalara yazma işlemi yapılamaz
#UnsupportedOperation: not writable
dosya.close()

dosya=open("metin_dosyasi.txt","r+")
print(dosya.read())
dosya.write("İyiyim\n") 
dosya.seek(0)
print(dosya.read())
dosya.close()

dosya=open("metin_dosyasi.txt","a")
dosya.write("Dersler başladı\n")
#print(dosya.read()) #a+ kipiyle açılan dosyalarda okuma işlemi yapılamaz
#UnsupportedOperation: not readable
dosya.close()


dosya=open("metin_dosyasi.txt","a+")
dosya.write("Python ile dosyalar konusunu işliyoruz\n")
dosya.seek(0)
print(dosya.read()) 
dosya.close()


a=["1.2","3.4"]
b=[]
c=[]
for sayi in a:
    b.append(sayi.split(".")[0])
    c.append(sayi.split(".")[1])
print("b:",b,"c:",c)


#Soru:
#Bir dosyayı sıfırdan oluşturup hem okuma hem de yazma modunda açalım
#açma Kipi : w+
#sayılar : 10 tane 1 ile 20 arasındaki random sayı tutacak
#Bu sayıları alt alta dosyaya yazdıralım
#Bu dosya içerisinde tek sayıları teksayilar isimli dosyaya, çift sayıları çift sayılar isimli dosyaya atayalım

with open("sayilar.txt","w+") as dosya:
    #with içerisinde dosya açık kalır, with dışına çıktığımız an dosya kapanır. Dosyayla çalışmaya devam edemeyiz. dosya.close() yazmamıza gerek yoktur
    from random import randint
    for i in range(10):
        dosya.write(str(randint(1,20))+"\n")
        
    dosya.seek(0)
    print(dosya.read())
    
    dosya.seek(0)
    print(dosya.readline())
    print(dosya.readline())
    print(dosya.readline())
    
    dosya.seek(0)
    print(dosya.readlines())
    
    dosya.seek(0)
    liste=dosya.readlines()
    
    print(liste)
    sayilar=[]
    for sayi in liste:
        sayilar.append(int(sayi.split("\n")[0]))
    print(sayilar)

print("Tek sayılar:")
with open("teksayilar.txt","w+") as dosya:
    for sayi in sayilar:
        if sayi%2==1:
            dosya.write(str(sayi)+"\n")
    dosya.seek(0)
    print(dosya.read())

print("Çift sayılar:")
with open("ciftsayilar.txt","w+") as dosya:
    for sayi in sayilar:
        if sayi%2==0:
            dosya.write(str(sayi)+"\n")
    dosya.seek(0)
    print(dosya.read())
    
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
    print(dosya.read()) #kursör dosyanın sonundadır
    
    dosya.seek(0) #kursörü dosyanın başındadır
    liste=dosya.readlines()
    print(liste)
    
isimler=[]
notlar=[]
for veri in liste:
    isimler.append(veri.split(",")[0])
    n=veri.split(",")[1]
    notlar.append(n.split("\n")[0])
print(isimler,notlar)

print("Geçenler:")
with open("geçenler.txt","w+") as dosya:
    for i in range(len(notlar)):
        if notlar[i]!="FF":
            dosya.write(isimler[i]+"\n")
    dosya.seek(0)
    print(dosya.read())

print("Kalanlar:")
with open("kalanlar.txt","w+") as dosya:
    for i in range(len(notlar)):
        if notlar[i]=="FF":
            dosya.write(isimler[i]+"\n")
    dosya.seek(0)
    print(dosya.read())




 
    
    
    