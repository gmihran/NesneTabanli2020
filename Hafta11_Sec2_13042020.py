# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 14:35:50 2020

@author: Gözde Mihran Altınsoy
"""

#Vize Sınavı: 25 Nisan Cumartesi-27 Nisan Pazartesi

#Nesne tabanlı programlama nedir ve neden kullanılır? Örnekle açıklayınız.
#Nesne tabanlı (yönelimli) programlamanın artıları nelerdir?
#Neden kullanıyoruz? 
#Nesne tabanlı programlamanın yapısını ve özelliklerini araştırınız.
#Bununla ilgili bir örnek oluşturunuz.

#Class Örnekler
#Bitki --> Çiçek
#Ürün
#Virüs
#Bilgisayar --> Dizüstü,Masaüstü,Mini
#Taşıt
#Canlı --> Hayvan, İnsan, Bitki
#Personel
#Meslekler


#Inheritance (miras alma, kalıtım)

#class'ların ilk harfi büyük harfle başlar
class Canli():
    
    def __init__(self,hucreturu="",solunum="Oksijenli"):
        #Yapıcı (Constructor) fonksiyonu çalıştı
        self.solunum=solunum #Oksijensiz
        self.ureme="Eşeyli" #Eşeysiz
        self.hucreyapisi="çok hücreli" #tek hücreli
        self.hucreturu=hucreturu  #bitki hücresi,hayvan hücresi
        self.hareket=""
        #Attribute (nitelik,özellik)

class Bitki(Canli):
    def __init__(self):
        self.hucreyapisi="Çok hücreli"
        self.solunum="fotosentez"
        self.hucreturu="bitki hücresi"
        self.hareket="pasif"
        print("Yapıcı çalıştı")
        
    def GetSolunum(self):
        return self.solunum
    

class Hayvan(Canli):
    def __init__(self,beslenme="Etçil",bacaksayisi=4):
        self.beslenme=beslenme #Etçil #Otçul
        if bacaksayisi>0:
            self.bacaksayisi=bacaksayisi
        else:
            self.bacaksayisi=4
            #Hatalı giriş yapılırsa 4 değeri atanır.
            print("Hatalı giriş yapıldı. Bacak sayısı 1'den küçük olmaz")
        self.hareket="aktif"
        self.hucreturu="hayvan hücresi"
    def __str__(self):
        return "Beslenme:{}\nBacak sayısı:{}\nHareket:{}\nHücre türü:{}".format(self.beslenme,self.bacaksayisi,self.hareket,self.hucreturu)
    def GetBacakSayisi(self):
        return self.bacaksayisi
    
    def GetBacakSayisi2(self):
        print("Bacak sayısı:",self.bacaksayisi)
        
    def SetBacakSayisi(self,bacaksayisi):
        self.bacaksayisi=bacaksayisi
        
    def SetGetBacakSayisi2(self,bacaksayisi):
        self.bacaksayisi=bacaksayisi
        return self.bacaksayisi

hayvan4=Hayvan()
hayvan4.SetBacakSayisi(2)
print(hayvan4.GetBacakSayisi())

print(hayvan4.SetGetBacakSayisi2(4))

hayvan4.GetBacakSayisi2()

hayvan5=Hayvan(bacaksayisi=-1)
print(hayvan5.bacaksayisi)

print()
bitki=Bitki() 
print(bitki.solunum)
print(bitki.GetSolunum())
print(bitki.hucreyapisi)

bitki2=Bitki()
print(bitki2.hucreyapisi)

#canli nesne(örnek)
canli=Canli()

print()

hayvan=Hayvan()

#<__main__.Hayvan object at 0x0000016EA6B2F9C8>
print(hayvan)
print()

hayvan2=Hayvan("Otçul",2)
print(hayvan2)

print()

hayvan3=Hayvan(bacaksayisi=2)
print(hayvan3)













