# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 09:58:11 2020

@author: Gözde Mihran Altınsoy

Nesne Tabanlı Programlama
"""
class Araba():
    model="Renauld Clio"
    renk="Beyaz"
    
araba1=Araba()
print("Model:",araba1.model," Renk:",araba1.renk)
araba1.renk="Kırmızı"
print("Model:",araba1.model," Renk:",araba1.renk)
print(araba1)
#<__main__.Araba object at 0x00000178008AA3C8>

class Kedi(): #class (sınıf)
    #cinsi="Tekir" #türü
    #renk="Sarı"
    #cinsiyet="Dişi"
    print("Kedi nesnesi oluşturuldu")
    
    def __init__(self,cins="Tekir",renk="Sarı",cinsiyet="Dişi"):
        #self hangi nesneye işaret ettiğimi, hangi nesne üzerinde tanımlama yaptığımı ifade eder.
        self.cinsi=cins
        self.renk=renk
        self.cinsiyet=cinsiyet
        print("init çalıştı.")
        
    def __str__(self):
        #nesneyi print fonksiyonu ile yazdırmak istediğimizde yani nesneyi çağırdığımız bu fonksiyon çalışır 
        #return kullanmak zorundayız
        return "Cinsi:{}\nRengi:{}\nCinsiyeti:{}".format(self.cinsi,self.renk,self.cinsiyet)
    #return yapılan değerin mutlaka string değer olması gerekir
        
    def GetOzellik(self):
        print("Cinsi:",self.cinsi," Rengi:",self.renk," Cinsiyeti:",self.cinsiyet)
        
    def GetOzellik2(self):
        print("Cinsi:",self.cinsi,"\nRengi:",self.renk,"\nCinsiyeti:",self.cinsiyet)
        
    def SetOzellik(self,cins,renk,cinsiyet):
        self.cinsi=cins
        self.renk=renk
        self.cinsiyet=cinsiyet
        
    def SetCinsi(self,cinsi):
        self.cinsi=cinsi

kedi1=Kedi() #kedi1 objesi (nesne) türetildi

print("Cinsi:",kedi1.cinsi," Rengi:",kedi1.renk," Cinsiyeti:",kedi1.cinsiyet)
kedi1.cinsi="İran"
kedi1.renk="Beyaz"
kedi1.cinsiyet="Erkek"
print("Cinsi:",kedi1.cinsi," Rengi:",kedi1.renk," Cinsiyeti:",kedi1.cinsiyet)

kedi2=Kedi("Siyam","Siyah","Erkek")
#print("Cinsi:",kedi2.cinsi," Rengi:",kedi2.renk," Cinsiyeti:",kedi2.cinsiyet)
kedi2.GetOzellik()
kedi2.GetOzellik2()

kedi2.SetOzellik("Van", "Beyaz", "Dişi")
kedi2.GetOzellik()

kedi2.SetCinsi("Tekir")
print("Cinsi:",kedi2.cinsi)

print()
print(kedi2)
#Eğer __str__ fonksiyonu tanımlanmaz ise aşağıdaki çıktıyı verir. Ama adres bilgisi farklı olabilir.
#<__main__.Kedi object at 0x00000178008AA308>

print()

class Ogrenci():
    print("Ogrenci objesi oluşturuldu")
    def __init__(self,no=0,ad="",soyad="",yas=0):
        #self Ogrenci class'ından türetilen nesneye işaret ediyor. 
        self.no=no #self.no nesneye ait olan no değeridir. 
        #no değeri dışarıdan bu fonksiyona ilk gönderilen değerdir
        self.ad=ad
        self.soyad=soyad
        self.yas=yas
        print("init çalıştı")
    def __len__(self):
        return self.yas
    def __del__(self):
        print("Kayıt silindi")
    def __str__(self):
        return "No:{} Ad:{} Soyad:{} Yaş:{}".format(self.no,self.ad,self.soyad,self.yas)
        
ali=Ogrenci()
print("Ali no:",ali.no)

ayse=Ogrenci(1,"Ayşe","Akın",20) 
print("Ayşe no:",ayse.no)

print(len(ayse))

print(ayse)

#del ayse
#del fonksiyonu ile nesne silinebilir.
#Ama bu sırada bize herhangi bir çıktı veya döndürdüğü değer yoktur
#Biz __del__() fonksiyonunu tanımlayarak özelleştirebiliriz

#print(ayse)
#:::Hata mesajı:::
#NameError: name 'ayse' is not defined
#ayse nesnesi silindiği için hata oluştu.



