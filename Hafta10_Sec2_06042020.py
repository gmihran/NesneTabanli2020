# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 15:02:56 2020

@author: Gözde Mihran Altınsoy
"""

class Arac():
    model="Renault Clio"
    renk="Kırmızı"
    yil=2018

arac1=Arac()
print(arac1.model)
print(arac1.renk)
print(arac1.yil)


print()

class Kedi():
    
    #cinsi="Tekir"
    #renk="Sarı"
    #cinsiyet="Dişi"
    
    print("Kedi nesnesi oluşturuldu")
    
    def __init__(self,cins="Tekir",renk="Sarı",cinsiyet="Dişi"):
        self.cinsi=cins
        self.renk=renk
        self.cinsiyet=cinsiyet
        print("init fonksiyonu çalıştı")
        
    def __str__(self):
        print("__str__ fonksiyonu çalıştı")
        return "Cinsi:{} Renk:{} Cinsiyet:{}".format(self.cinsi,self.renk,self.cinsiyet)
        #str fonksiyonu nesne çağrıldığı an çalışır. print ile yazdırmaya çalıştırdığımızda __str__() fonksiyonunun varsayılan değeri türediği class ve bulunduğu adrestir.
        #Bunu özelleştirmek istersek bu şekilde tanımlayabiliriz.
        #return olmak zorundadır
        #return ile döndürdüğümüz değer string türünde olmalıdır.
        
    def GetOzellik(self):
        print("Cinsi:",self.cinsi," Renk:",self.renk," Cinsiyet:",self.cinsiyet)
        
    def GetCinsiyet(self):
        print("Cinsiyet:",self.cinsiyet)
        
    def SetOzellik(self,cins,renk,cinsiyet):
        self.cinsi=cins
        self.renk=renk
        self.cinsiyet=cinsiyet

kedi1=Kedi("İran","Sarı","Dişi")
print("Cinsi:",kedi1.cinsi," Renk:",kedi1.renk," Cinsiyet:",kedi1.cinsiyet)

kedi1.cinsi="İran"
kedi1.renk="Beyaz"
kedi1.cinsiyet="Erkek"
print("Cinsi:",kedi1.cinsi," Renk:",kedi1.renk," Cinsiyet:",kedi1.cinsiyet)

kedi2=Kedi()
print("Cinsi:",kedi2.cinsi," Renk:",kedi2.renk," Cinsiyet:",kedi2.cinsiyet)


kedi3=Kedi()
print(kedi3.cinsi)

kedi3.cinsi="Van"
print(kedi3.cinsi)

kedi3.GetOzellik()

kedi3.GetCinsiyet()

kedi2.GetOzellik()

kedi2.SetOzellik("Siyam", "Siyah", "Erkek")
kedi2.GetOzellik()

print(kedi2) 
#__str__() fonksiyonu tanımlanmazsa bu nesnenin hangi class'a ait olduğunu ve adresini verir.
#<__main__.Kedi object at 0x00000178007A5D08>


class Insan():
    
    def __init__(self,ad="",soyad="",yas=0,boy=0):
        self.ad=ad
        self.soyad=soyad
        self.yas=yas
        self.boy=boy
        
    def __str__(self):
        return "Ad:{}\nSoyad:{}\nYaş:{}\nBoy:{}\n".format(self.ad,self.soyad,self.yas,self.boy)
    
    def __len__(self):
        #len fonksiyonu tanımlanmazsa nesneye len fonksiyonu uygulanamaz
        #len fonksiyonuna nesneyi parametre olarak gönderdiğimizde bu fonksiyon çalışır
        return self.yas
    
    def __del__(self):
        print("Değer silindi")
        
insan1=Insan()
print(insan1)

insan2=Insan("Ayşe","Gök",20,170)
print(insan2)

print(len(insan2))

del insan2
#print(insan2)

import datetime
tarih = datetime.date.today()
print(tarih)

class Cikolata():
    
    def __init__(self,turu="sütlü",agirlik=100,stt=tarih):
        self.tur=turu
        self.agirlik=agirlik
        self.stt=stt #Son tüketim tarihi
        
    def __str__(self):
        return "Türü:{}\nAğırlık:{}\nSon Tüketim Tarihi::{}".format(self.tur,self.agirlik,self.stt)
    
    def GetTutar(self):
        agirliklar=[30,40,50,60,70,100]
        tutar=[4,5,6.5,7,8,10]
        for i in range(len(agirliklar)):
            if self.agirlik==agirliklar[i]:
                self.tutar=tutar[i]
                return self.tutar
        
        
bolsutlu=Cikolata()
print(bolsutlu.tur)        

print(bolsutlu.GetTutar())

print()

bitter=Cikolata("bitter",60,"2021-04-06")
print(bitter.tur)

print(bitter)        
        
print(bitter.GetTutar())

print()
fındıklı=Cikolata("fındıklı",55,"2022-05-01")
print(fındıklı)
print(fındıklı.GetTutar())

if fındıklı.GetTutar()==None:
    print("Değer bulunamadı")
else:
    print(fındıklı.tutar)

if bitter.GetTutar()==None:
    print("Değer bulunamadı")
else:
    print(bitter.tutar)

