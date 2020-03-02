# -*- coding: utf-8 -*-
"""
Created on Mon Mar  2 15:00:00 2020

@author: gozdemihranaltinsoy
"""

#Fonksiyonlar
"""
Fonksiyon kullanmak sayesinde:

*Aynı kodu defalarca yazmak gerekmez.
*Tekrarlama yüzünden doğacak hatalar ortadan kalkar.
*Bellek (RAM) gereksiz yere dolmaz. 
*Kod parçası onlarca kere tekrarlanmak yerine bir kere yazılır.
*Programcı küçük ayrıntılara tekrar tekrar kafa yormak zorunda kalmaz.
*İşleri küçük birimlere bölmek, programlama hatalarını bulmayı kolaylaştırır.
*Programlama dilinin çekirdek tanımında bulunmayan üst seviye işlemleri tek komutla yapmayı sağlar.
*Fonksiyon kütüphaneleri, uzmanlaşmış programcılar tarafından hızlı ve verimli hale getirilebilir.
Bu faydalar sadece Python değil, her türlü programlama dili için geçerlidir.
def fonksiyon_adı(parametre1,parametre2..... (opsiyonel)):
    # Fonksiyon bloğu
    Yapılacak işlemler
    # dönüş değeri - Opsiyonel
"""

#Kendisine gönderilen iki sayının toplamını bulan fonksiyonu yazınız ve fonksiyonu çağırınız.
#%%
def topla(s1,s2):
    print(s1+s2)
topla(5,6)
topla(5.2,6.4)
topla(4,2.3)


#%%
##Fonksiyonun içerisinde girilen iki sayının toplamını bulan fonksiyonu yazınız ve fonksiyonu çağırınız.
#%%
def topla():
    s1=eval(input("Sayı 1:"))
    s2=eval(input("Sayı 2:"))
    #eval : Değişken türüne kendisi karar verir. 
    #Tamsayı girilirse int, ondalıklı sayı girilirse float olarak saklar
    print(s1+s2)
topla()

#%%
#Girilen iki sayının birbirine tam bölünüp bölünemediğinin
#çıktısını veren kodu yazınız
#Mod alma : % işareti ile kontrol edilir
#Eğer mod sonucu 0 ise "bölünebilir", değilse "bölünemez"
#%%
def mod():
    bolunen=int(input("Bölünen:"))
    bolen=int(input("Bölen:"))
    if bolunen%bolen==0:
        print("Bölünebilir")
    else:
        print("Bölünemez")
mod()
#%%
"""
1.Başla
2.Yaz "Sayı Gir"
3.Oku s1
4.Yaz "Sayı Gir"
5.Oku s2
6.Eğer s1%s2=0 ise Yaz "Bölünebilir"
  Değilse Yaz "Bölünemez"
7.Bitir    
"""

#%%
print(10//3) #3
print(10%3)  #1
print(10/3)  #3.3333333333333335

#%%
#Klavyeden girilen para miktarını banknotlara ayıran programı yazınız. 
#Banknotlar:200,100,50,20,10,5,1
#Ör: 
#26 -> 1 tane 20, 1 tane 5, 1 tane 1
#358-> 1 tane 200, 1 tane 100, 1 tane 50, 1 tane 5, 3 tane 1
#555 -> 2 tane 200, 1 tane 100, 1 tane 50, 1 tane 5
#%%
banknotlar=[200,100,50,20,10,5,1]
miktarlar=[]
tutar=int(input("Para:"))
tutaryedek=tutar
for i in banknotlar:
    miktarlar.append(tutaryedek//i)
    tutaryedek=tutaryedek%i
for i in range(0,7):
    if miktarlar[i]!=0:
        print(miktarlar[i]," tane ",banknotlar[i])
#%%
"""
1.Başla
2.banknotlar=[200,100,50,20,10,5,1]
3.miktarlar=[]
4.Oku tutar
5.tutaryedek=tutar
6.Döngü başlat i in banknotlar
7.miktarlar.append(tutaryedek//i)
8.tutaryedek=tutaryedek%i
9.Döngü bitir (i)
10.Döngü başlat i=0,6,1
11.Eğer miktarlar[i]!=0 ise Yaz miktarlar[i]," tane ",banknotlar[i]
12.Döngü bitir (i)
13.Bitir
"""
#range(7) veya range(0,7) kullanılabilir

#Bu örneği fonksiyon haline getirelim:
#%%   
def banknot(tutar):
    banknotlar=[200,100,50,20,10,5,1]
    miktarlar=[]
    for i in banknotlar:
        miktarlar.append(tutar//i)
        tutar=tutar%i
    for i in range(0,7):
        if miktarlar[i]!=0:
            print(miktarlar[i]," tane ",banknotlar[i])

tutar=int(input("Para:"))
banknot(tutar)
#%%
demet=(1,2,3)
liste=[1,2,3]

demet=(3,4,5) #bütün haliyle değişiklik mümkündür. Parça halinde değişiklik olamaz.
#demet[0]=6 #hata oluşur. Demetler değiştirilemez. Sadece okunabilir.
#Listede fonksiyon çeşitliliği demete göre daha fazladır.
liste[0]=5 #liste değiştirilebilir

#Sözlükler (dictionary)
sayilar={1:"bir",2:"iki",3:"üç",4:"dört",5:"beş"}
print(sayilar.items())
print(sayilar.keys())
print(sayilar.values())
print(sayilar[1])
print(sayilar.get(1,"sayı bulunamadı")) #Çıktı: bir
print(sayilar.get(6,"sayı bulunamadı")) #Çıktı: sayı bulunamadı
sayilar.setdefault(1,"BİR") #sözlükte bu değer olduğu için 1 değeri değişmedi
sayilar.setdefault(6,"altı") #sözlükte bu değer olmadığı için 6 değerini sözlüğe ekler

sayilar[7]="yedi"
print(sayilar)

sayilar.pop(7)
print(sayilar.items())

sayilar.pop(2)
print(sayilar)
#%%
#sozluk={key1:value1,key2:value2:...}
#sozluk={anahtar1:değer1,anahtar2:değer2:...}

sozluk={"elma":"apple","muz":"banana","barış":"peace","kuzey":"north","güney":"south","bilgisayar":"computer"}
deger=input("Kelime:")
print(sozluk.get(deger,"bulunamadı"))
#print(sozluk[deger])
try:
    print(sozluk[deger])
except:
    durum=input("Kelime bulunmadı. Sözlüğe eklemek ister misiniz? E/H:")
    if durum=="E":
        deger2=input("İngilizce karşılığı:")
        sozluk[deger]=deger2
print(sozluk)
#%%

gün=input("Gün:").title()
#title girilen kelimenin baş harfini büyük harf, diğer harflerini küçük harf yapar

#%%
#Girilen günün haftanın kaçıncı günü olduğunu veren program
#Ör/ Kullanıcı Pazartesi girdiğinde 1,
#ÖR/ Kullanıcı Pazar girdiğinde 7 çıktısını verecek
#sözlük yapısını kullanıyoruz:
#farklı çözümlerde kullanılabilir
#sozluk={key1:value1,key2:value2:...}
#sozluk={anahtar1:değer1,anahtar2:değer2:...}
günler={"Pazartesi":1,"Salı":2,"Çarşamba":3,"Perşembe":4,"Cuma":5,"Cumartesi":6,"Pazar":7}
gün=input("Gün:")
gün=gün.replace("I","ı").replace("İ","i").title()
print(gün)
print(günler.get(gün,"hatalı değer"))
#%%
"""
1-Pazartesi
8-Pazartesi
7-Pazar
14-Pazar
"""
#%%
günler={1:"Pazartesi",2:"Salı",3:"Çarşamba",4:"Perşembe",5:"Cuma",6:"Cumartesi",0:"Pazar"}
deger=int(input("Gün değeri:"))
print(günler.get(deger%7,"Bulunamadı"))

#%%
#Listeyi sıralama:
liste=[10,45,30,23,27,2]
liste.sort() #Küçükten büyüğe sıralama
print(liste)
liste.sort(reverse=True) #Büyükten küçüğe sıralama
print(liste)
#%%
#Oyun:
#Listemiz 6 tane rastgele sayıdan oluşsun
#Sayı aralığı 1-45 arasında
#Kullanıcıdan 5 tane sayı isteyelim kaç tane sayıyı doğru tahmin ettiğini yazdıralım
#Not: Üretilen sayılar benzersiz olmalı ve sayılar sıralı olmalı
#%%
import random
rastgele=[]
for i in range(6):
    while True:
        kontrol=False
        sayi=random.randint(1,45)
        if sayi in rastgele:
            kontrol=True
        if kontrol==False:
            break
    rastgele.append(sayi)
rastgele.sort()
print(rastgele)
sayılar=[]
miktar=0
for i in range(5):
    sayılar.append(int(input("Sayı:")))
for i in rastgele:
    if i in sayılar:
        print(i)
        miktar+=1
print("Miktar:",miktar)




#%%
#Girilen sayının 2 ile 9 arasındaki rakamlara tam bölünüp bölünmediğinin çıktısını veren program
#Ör: 45
#2 bölünenemez
#3 bölünür
#4 bölünemez
#5 bölünür
#6 bölünemez
#7 bölünemez
#8 bölünemez
#9 bölünür
#%%




#%%
#Sayının 2-9 arasındaki sayılardan tam bölenlerini yazdıralım




#%%
#Çalışma Sorusu:
#Çarpım tablosu
#aralarda tab boşluğu var
#1*1=1    2*1=2    3*1=3    4*1=4    5*1=5
#1*2=2    2*2=4......................5*2=10
#..........................................
#1*10=10 2*10=20   3*10=30  4*10=40  5*10=50    
#%%


#%%
#Modüller (Metodlar - Fonksiyonlar)

#Kendisine gönderilen iki sayının toplamını hesaplayan metod:
#%%

#%%
#Kendisine gönderilen sayının faktöriyelini hesaplayan metod:
#%%


#%%
#Sayının karesini ekrana yazdıran metod:
#%%


#%%
#Kendisine gönderilen sayı ve üs değerlerine göre üssünü hesaplayıp
#ekrana yazdıran metod:
#%%

#%%
#Rastgele 1 ile 100 arasında üretilen 10 sayının toplamını döndüren (return) metod:
#%%

#%%
#10 sayısının 3 sayısına bölümünden kalanı ekrana yazdıran metod:
#%%

#%%
#Kendisine gönderilen değer kadar kendisine gönderilen
#min ve mak değerler arasında random değer üretip
#bu değerleri ana metoda döndüren metod:
#Parametre 3 değer, döndürülen random değerler (liste)
#%%


#%%









