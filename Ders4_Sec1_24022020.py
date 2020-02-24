# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 10:11:44 2020

@author: gozdemihranaltinsoy
"""

#Girilen ismin içinde a harfi var mı diye 
#kontrolünü gerçekleştiren kodu yazınız
#kelimenin tüm harflerini kontrol ediniz.
#Her harften sonra;
#"A/a harfidir", "A/a harfi değildir" diye çıktı verilecek

#Ör:Ada girilseydi
#Çıktı:
#A/a harfidir
#A/a harfi değildir
#A/a harfidir
#%%
isim=input("İsim:")
for harf in isim:
    if harf=="a" or harf=="A":
        #or ile ikiisinden biriyse anlamı kattık
        print(harf," A/a harfidir")
    else:
        print(harf," A/a harfi değildir")        
#%%    
#Girilen ismin içinde a harfi var mı diye 
#kontrolünü gerçekleştiren kodu yazınız
#kelimenin tamamını kontrol ediniz. 
#"A/a harfi var" "A harfi yok" şeklinde çıktı 1 kere oluşacak
#%%
kontrol=False
isim=input("İsim:")
for harf in isim:
    if harf=="A" or harf=="a":
        kontrol=True
        break
if kontrol:
    print("A/a harfi vardır")  
else:
    print("A/a harfi yoktur")      
#%%
#Girilen ismin içinde a harfinin kaçıncı sıralarda olduğunun
#ve a harfinin miktarının çıktısını verecek olan programı yazınız.
#Ör: Masa girilirse;
#Çıktı: "[2,4] harfleridir. 2 tanedir."
#Ör: Sevgi girilirse;
#Çıktı: "Yoktur"
#%%
isim=input("İsim:")
liste=list() #liste=[] 
#boş liste oluşturuldu
sayac=0
for i in range(0,len(isim)): 
    if isim[i]=="a" or isim[i]=="A":
        sayac+=1
        liste.append(i+1)
if sayac>0: #if len(liste)>0:
    print(liste," harfleridir.",sayac," tanedir")  
else:
    print("Yoktur")      
#%%
    
    
#Girilen ismin içinde klavyeden girilen harfin kaçıncı sıralarda olduğunu
#ve bu harfin miktarını çıktı olarak verecek programı yazınız.
#Ör: kalem ve e harfi girilirse;
#Çıktı: "[4] harfidir. 1 tanedir."
#Ör: kalem ve i harfi girilirse;
#Çıktı: "Yoktur"
#Ör: adana ve a harfi girilirse;
#Çıktı: "[1,3,5] harfidir. 3 tanedir."
#%%
isim=input("İsim:")
harf=input("Harf:")
liste=list() #liste=[] 
#boş liste oluşturuldu
sayac=0
for i in range(0,len(isim)): 
    if isim[i].upper()==harf.upper():
        #upper() fonksiyonu ile "i" harfini "I" harfi olarak değiştirir
        sayac+=1
        liste.append(i+1)
if sayac>0: #if len(liste)>0:
    print(liste," harfleridir.",sayac," tanedir")  
else:
    print("Yoktur")
    
#Örnek çıktılar:   
#upper() fonksiyonu ile i harfi ile ilgili doğru sonuçlar alamayabiliriz.
"""
İsim:ığdır

Harf:i
[1, 4]  harfleridir. 2  tanedir
"""
    
"""
İsim:isim

Harf:İ
Yoktur
"""

"""
İsim:ikiz

Harf:i
[1, 3]  harfleridir. 2  tanedir
"""
#%%    
"""
Klavyeden girilen kelimenin içinde bulunan sesli harflerden 
kaç tane bulunduğunun çıktısını veren programı Python diliyle kodlayınız.
Ör: Beykoz Üniversitesi
miktar=[0,3,0,3,1,0,0,1]
e->3
i->3
o->1
ü->1
Ör: Bilgisayar
miktar=[2,0,0,2,0,0,0,0]
a-->2
i-->2
"""
#%%
#sesliharfler=["a","e","ı","i","o","ö","u","ü"]
#Sadece sesli harfler
#sesli="aeıioöuü" #string
sesliharfler=["a","e","ı","i","o","ö","u","ü"]
kelime=input("Kelime:")
miktar=[]
for i in sesliharfler:
    sayac=0
    #her harf değişiminde sayacı sıfırladık ki her harf kendi miktarını tutabilsin
    for j in kelime:
        if i==j:
            sayac+=1
    miktar.append(sayac)
print(sesliharfler,miktar)
for i in range(0,len(sesliharfler)):
    if miktar[i]>0: #if miktar[i]!=0:
        print(sesliharfler[i],"->",miktar[i])
        
    
#%%
"""
Algoritması:
1.Başla
2.Yaz "Kelime:"
3.Oku kelime   
4.sesliharfler=["a","e","ı","i","o","ö","u","ü"]
5.miktar=[]
6.Döngü başlat i in sesliharfler
7.sayac=0
8.Döngü başlat j in kelime
9.Eğer i==j ise sayac+=1
10.Döngü bitir (j)
11.miktar.append(sayac)
12.Döngü bitir (i)
13.Yaz sesliharfler,miktar
14.Bitir
    
    
"""    

#%%
"""
Taş - Kağıt - Makas Oyunu
Bilgisayar taş, kağıt ve makas değerlerinden 
birini random olarak seçecek (metin veya sayı 
ile tutabilirsiniz). Oyun aşağıda belirtmiş 
olduğum kurallara göre gerçekleşecek. 
Taş-kâğıt-makas, genellikle iki oyuncuyla ve 
üç durumdan birinin seçilmesiyle oynanan bir 
el oyunudur. Taş makası, makas kağıdı, kâğıt da 
taşı yener. Eğer oyuncular aynı durumu seçerse 
oyun berabere biter. 
Kazanma
Taş, makası kırarak yener.
Kağıt, taşı sararak yener.
Makas, kağıdı keserek yener.
Belirlenen skora ilk ulaşan oyunu kazanır. İstenirse tek seferli oyunlar da oynanabilir.
Hak ve skor planlamasını da dilediğiniz gibi yapabilirsiniz.
Açıklama: Python'da random sayı üretmek için;
import random #random sınıfını projenize 
dahil eder
sayı=random.randint(1,3) #1 ile 3 arasında 
random bir sayı üretip bu sayıyı sayı değişkenine 
atar.
degerler=["taş","kağıt","makas"]

    
"""
import random

degerler=["taş","kağıt","makas"]

while True:

    pcskor=0
    kullaniciskor=0
    
    while True: #sonsuz döngü başladı
    
        #1.yol:
        pc=random.choice(degerler)
        #degerler listesinden rastegele bir değer getirir
        
        #2.yol:
        deger=random.randint(0,2)
        #0 ile 2 arasında rastgele bir değer getirir
        pc=degerler[deger]
        #degerler listesinden bu değer indisindeki değeri pc değişkeninde tutarız
        
        secim=int(input("1-Taş 2-Kağıt 3-Makas 1/2/3:"))
        kullanici=degerler[secim-1]
        
        print("Pc:",pc)
        
        """
        Taş, makası kırarak yener.
        Kağıt, taşı sararak yener.
        Makas, kağıdı keserek yener.
        """
        
        if (pc=="taş" and kullanici=="makas") or (pc=="kağıt" and kullanici=="taş") or (pc=="makas" and kullanici=="kağıt"):
            pcskor+=1
            print("Pc kazandı Skor:",kullaniciskor,"-",pcskor)
            
        elif pc==kullanici:
            print("Berabere")
        else:
            kullaniciskor+=1
            print("Tebrikler kazandınız. Skor:",kullaniciskor,"-",pcskor)
            
        if pcskor==3 or kullaniciskor==3:
            break
    if kullaniciskor==3:
        print("Kazandınız.")
    else:
        print("Kaybettiniz.")   
    while True:
        tekrar=input("Tekrar oynamak ister misiniz. E/H:")
        if tekrar=="H":
            break
        elif tekrar=="E":
            print("Oyun tekrar başlatılıyor..")
            break
        else:
            print("Hatalı giriş")
    if tekrar=="H":
        break
    


######################################
#Bundan sonraki örneklere haftaya devam edeceğiz...        



#%%
#Girilen iki sayının birbirine tam bölünüp bölünemediğinin
#çıktısını veren kodu yazınız
#Mod alma : % işareti ile kontrol edilir
#Eğer mod sonucu 0 ise tam bölünebilir
#%%
#Klavyeden girinin para miktarını banknotlara ayıran programı 
#yazınız. 200,100,50,20,10,5,1
#%%

#Sözlükler (dictionary)
sozluk={"elma":"apple","muz":"banana","barış":"peace","kuzey":"north","güney":"south","bilgisayar":"computer"}
#kelime=input("Kelimeyi girin..:")
#print(sozluk[kelime])
print(sozluk.items())
print(sozluk.keys())
print(sozluk.values())
#items elma,apple
#key elma
#values apple

gün=input("Gün:").title()
#title girilen kelimenin baş harfini büyük harf, diğer harflerini küçük harf yapar

#%%
#Girilen günün haftanın kaçıncı günü olduğunu veren program
#Ör/ Kullanıcı Pazartesi girdiğinde 1,
#ÖR/ Kullanıcı Pazar girdiğinde 7 çıktısını verecek
#sözlük yapısını kullanıyoruz:
#farklı çözümlerde kullanılabilir

#%%
#Listeyi sıralama:
liste=[10,45,30,23,27,2]
liste.sort()
print(liste)
liste.sort(reverse=True)
print(liste)
#%%
#Oyun:
#Listemiz 6 tane rastgele sayıdan oluşsun
#Sayı aralığı 1-45 arasında
#Kullanıcının kaç tane sayıyı doğru tahmin ettiğini yazdıralım
#Not: Üretilen sayılar benzersiz olmalı ve sayılar sıralı olmalı
#%%


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