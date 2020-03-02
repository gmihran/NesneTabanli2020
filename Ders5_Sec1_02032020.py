# -*- coding: utf-8 -*-
"""
Created on Mon Mar  2 10:15:08 2020

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
    print("Toplam:",s1+s2)
topla(5,2)
#%%
##Fonksiyonun içerisinde girilen iki sayının toplamını bulan fonksiyonu yazınız ve fonksiyonu çağırınız.
#%%
def topla():
    s1=int(input("1.sayı:"))
    s2=int(input("2.sayı:"))
    print("Toplam:",s1+s2)
topla() 

#%%
#Girilen iki sayının birbirine tam bölünüp bölünemediğinin
#çıktısını veren kodu yazınız
#Mod alma : % işareti ile kontrol edilir
#Eğer mod sonucu 0 ise "bölünebilir", değilse "bölünemez"
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
def mod():
    s1=eval(input("Bölünen:"))
    s2=eval(input("Bölen:"))
    if s1%s2==0:
        print("Bölünebilir")
    else:
        print("Bölünemez")
mod()



#%%
#Klavyeden girilen para miktarını banknotlara ayıran programı yazınız. 
#Banknotlar:200,100,50,20,10,5,1
#Ör: 
#26 -> 1 tane 20, 1 tane 5, 1 tane 1
#358-> 1 tane 200, 1 tane 100, 1 tane 50, 1 tane 5, 3 tane 1
#555 -> 2 tane 200, 1 tane 100, 1 tane 50, 1 tane 5


#%%
liste=[200,100,50,20,10,5,1]
miktar=[]
para=int(input("Para:"))
parayedek=para
for i in liste:
    miktar.append(parayedek//i)
    parayedek=parayedek%i
#banknot miktarı 0 ise ekrana yazdırılmayacak
for i in range(0,len(liste)):
    #0-6 arasında i değeri alır
    if miktar[i]!=0:
        print(miktar[i]," tane ",liste[i])

#Bu örneği fonksiyon haline getirelim:
#%%   
def banknot(para):   
    #Parametre olarak tanımlanan para değeri main()'deki  para değerinin kopyasıdır. Kendisi değildir.     
    liste=[200,100,50,20,10,5,1]
    miktar=[]
    for i in liste:
        miktar.append(para//i) 
        #para//i ifadesi ile para değerinin i değerine bölümünün tam kısmını alırız
        para=para%i
        #para%i ifadesi ile para değerinin i değerine bölümünden kalanını alırız
    #banknot miktarı 0 ise ekrana yazdırılmayacak
    for i in range(0,len(liste)):
        #0-6 arasında i değeri alır
        if miktar[i]!=0:
            print(miktar[i]," tane ",liste[i])
para=int(input("Para:"))
banknot(para)
#%%
demet=(1,2,3)
liste=[1,2,3]

#Sözlükler (dictionary)
sayilar={1:"bir",2:"iki",3:"üç",4:"dört",5:"beş"}
print(sayilar)
print(sayilar[3]) #key=3 value="üç"
print(sayilar.items()) #items=keys-values çıktısını verir
print(sayilar.keys()) #dict_keys([1, 2, 3, 4, 5])
print(sayilar.values()) #dict_values(['bir', 'iki', 'üç', 'dört', 'beş'])


#%%
#sozluk={key1:value1,key2:value2:...}
#sozluk={anahtar1:değer1,anahtar2:değer2:...}

sozluk={"elma":"apple","muz":"banana","barış":"peace","kuzey":"north","güney":"south","bilgisayar":"computer"}
print(sozluk["elma"]) #apple
print(sozluk.get("elma")) #apple

#kelime=input("Kelimeyi girin..:")
#print(sozluk[kelime])

sozluk.pop("elma") #elma değerini siler
print(sozluk)
#print(sozluk["elma"]) #Hata: KeyError: 'elma'

print(sozluk.items())
print(sozluk.keys())
print(sozluk.values())
#items elma,apple
#key elma
#values apple

#Sözlüğe bir değer ekleyelim
sozluk["bir"]="one"
print(sozluk)

#Sözlüğe bir değer ekleyelim
sozluk["güneş"]="sun"
print(sozluk)
print(sozluk.items())

sozluk2=sozluk.copy() #sozluk sozluk2'ye kopyalandı
sozluk.clear() #sozluk içerisindeki değerler silindi
print(sozluk)
print(sozluk2)

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
gün=gün.replace("I","ı") 
gün=gün.title() 
#title() fonksiyonu I harfini i harfini dönüştürür
#Bunu engellemek için replace ile I harfini ı harfine dönüştürdük
print(gün)
#1.yöntem:
print(günler[gün])
#2.yöntem:
print(günler.get(gün))
"""
1-Pazartesi
8-Pazartesi
7-Pazar
14-Pazar
"""
#%%
günler={1:"Pazartesi",2:"Salı",3:"Çarşamba",4:"Perşembe",5:"Cuma",6:"Cumartesi",0:"Pazar"}
sayi=int(input("Değer:"))
sayi=sayi%7
print(günler.get(sayi,"Değer bulunamadı"))

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
for i in range(6): #i 0 ile 5 arasında değer alır 
    while True:
        kontrol=False
        sayi=random.randint(1,45)
        for j in rastgele:
            if j==sayi:
                kontrol=True
        if kontrol==False:
            #Listede olmayan bir değer üretilmişse while döngüsü kırılır
            break
    rastgele.append(sayi)   
rastgele.sort()
print(rastgele)
tahminler=[]
miktar=0
for i in range(5):
    tahminler.append(int(input("Tahmin:")))                
for i in rastgele:
    if i in tahminler:
        print(i)
        miktar+=1
print("Doğru tahmin sayısı:",miktar)                  
    

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
sayi=int(input("Sayı:"))
for bolen in range(2,10):
    if sayi%bolen==0:
        print(bolen,"bölünür")
    else:
        print(bolen,"bölünmez")

#%%
#Sayının 2-9 arasındaki sayılardan tam bölenlerini yazdıralım
sayi=int(input("Sayı:"))
for bolen in range(2,10):
    if sayi%bolen==0:
        print(bolen,end=" ")

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









