# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 15:00:19 2020

@author: Gözde Mihran Altınsoy
"""

class Oyuncu():
    def __init__(self,isim,rutbe):
        #Yapıcı (Constructor) fonksiyon
        self.isim=isim
        self.rutbe=rutbe
        self.guc=0
        self.puan=100
        #self.isim,self.rutbe,self.guc,self.puan Public değişkenlerdir (niteliklerdir). Bu değerlere dışarıdan ulaşılabilir.
        
        
        self.__ozel=1
        #__ozel Private bir attribute (nitelik)
        #Class'ın dışından bu değere erişilemez
        #Yani class izin vermedikçe bu değer okunamaz veya değiştirilemez
         #Veri gizleme için nitelik önüne __ konulur. Böylece nitelik private olur. 
        #Sadece sınıf içerisinden erişilebilir. Dışarıdan erişebilir değildir
        
        self._ozel=5
         #Buradaki yarı gizli olan niteliğe sınıf içinden veya dışından erişmemizi engelleyen veya zorlaştıran hiçbir mekanizma bulunmaz. Ama biz bir sınıf içinde tek alt çizgi ile başlayan bir öğe gördüğümüzde, bunun sınıfın iç işleyişine ilişkin bir ayrıntı olduğunu, sınıf dışından bu öğeyi değiştirmeye kalkışmamamız gerektiğini anlarız.
        
    def Set_ozel(self,ozel):
        if ozel>=1 and ozel<=10:
            self.__ozel=ozel
            
    def Get_ozel(self):
        return self.__ozel
    
    def hareket_et(self):
        print("Hareket ediliyor...")
        
    def __str__(self):
        return "İsim:{} Rütbe:{} Güç:{}".format(self.isim,self.rutbe,self.guc)
    
    def puan_arttir(self,puan):
        self.puan=self.puan+puan
        
    def puan_azalt(self,puan):
        self.puan=self.puan-puan
        
    def Get_puan(self):
        return "Puan:{}".format(self.puan)
    
    def Get_guc(self):
        #class_name değişkeni private değişkendir
        #Fonksiyonun dışına çıkınca bu değerin yaşam ömrü biter
        class_name=self.__class__.__name__
        return "{} nesnesinin güç değeri: {}".format(class_name,self.guc) 
   
    #Destructor (Yıkıcı) metot
    #Nesneleri yok etme – Garbage collection
    def __del__(self):
        class_name=self.__class__.__name__
        print(class_name,"objesi silindi")
        
class Usta(Oyuncu):
    #Child (Çocuk) constructor
    def __init__(self, isim, rutbe):
        super().__init__(isim, rutbe)
        self.guc=30
        
 
class Isci(Oyuncu):
    def __init__(self):
        #Geçersiz kılma (Overriding)
        self.guc=25
        self.puan=100
        
    def hareket_et(self):
        #Geçersiz kılma (Overriding)
        print("Hareket edildi.")
        
    def __str__(self):
        return "Güç:{}".format(self.guc)
    
class Asker(Oyuncu):
    def __init__(self,*args):
        Oyuncu.__init__(self,*args)
        self.guc=100
       
        
oyuncu=Oyuncu("oyuncu",1)

#oyuncu.__ozel=2
#private değerlere direk atama ile müdahale edilemez.
#print(oyuncu.__ozel)
#private değerlere direk ulaşılamaz.
#Private değişkenler Class dışında değiştirilemez ve görüntülenemez
#Değiştirilebilmesi ve görüntülenmesi için Class içerisinde tanımlanmış metotlara ihtiyacımız vardır.


print("Özel:",oyuncu.Get_ozel())

oyuncu.Set_ozel(2)
print("Özel:",oyuncu.Get_ozel())

oyuncu.Set_ozel(11)
print("Özel:",oyuncu.Get_ozel())

print(oyuncu.guc)
oyuncu.hareket_et()

usta=Usta("usta",5)
print(usta.guc)
print(usta.hareket_et())
print(usta)

isci=Isci()
isci.isim="işçi"
print(isci.isim)
isci.hareket_et()

print(oyuncu)

print(isci)

asker=Asker("asker",10)
print(asker.guc)

print("Puan:",asker.puan)

asker.puan_arttir(20)
print("Puan:",asker.puan)

isci.puan_azalt(15)
print("Puan:",isci.puan)

print(isci.Get_puan())

print(asker.Get_puan())

print(asker.Get_guc())

print(asker._ozel)
asker._ozel=15
print(asker._ozel)
    
print(asker)

del asker    
del isci
#Nesneleri yok etme – Garbage collection (Çöp Toplama)
#Python’un periyodik olarak kullanımda olmayan bellek bloklarını sildiği süreçtir.
#Bir nesnenin referans sayısı sıfıra ulaştığında, Python otomatik olarak toplar.

#print(isci)

asker=Asker("asker",1)
asker2=asker
asker3=asker

print(id(asker),id(asker2),id(asker3))

del asker
print(id(asker2))
del asker2
del asker3

    
    