# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 09:59:33 2020

@author: Gözde Mihran Altınsoy
"""

class Oyuncu():
    def __init__(self,isim,rutbe):
        self.isim=isim
        self.rutbe=rutbe
        self.guc=0
        self.puan=100
        #self.isim,self.rutbe,self.guc,self.puan Public değişkenlerdir (niteliklerdir). Bu değerlere dışarıdan ulaşılabilir.
        
        self.__gizli=0  
        #Veri gizleme için nitelik önüne __ konulur. Böylece nitelik private olur. 
        #Sadece sınıf içerisinden erişilebilir. Dışarıdan erişebilir değildir
        
        self._gizli=1
         #Buradaki yarı gizli olan niteliğe sınıf içinden veya dışından erişmemizi engelleyen veya zorlaştıran hiçbir mekanizma bulunmaz. Ama biz bir sınıf içinde tek alt çizgi ile başlayan bir öğe gördüğümüzde, bunun sınıfın iç işleyişine ilişkin bir ayrıntı olduğunu, sınıf dışından bu öğeyi değiştirmeye kalkışmamamız gerektiğini anlarız.
        
    def Get_gizli(self):
        print("Gizli yazdırılıyor.",self.__gizli)
        
    def Set_gizli(self,gizli):
        if (gizli>=0 and gizli<=10):
            self.__gizli=gizli
    
    def hareket_et(self):
        print("Hareket ediliyor...")
        
    def puan_kazan(self,puan):
        print("Puan arttırılıyor...")
        self.puan=self.puan+puan
        
    def puan_kaybet(self,puan):
        print("Puan azaltılıyor...")
        self.puan=self.puan-puan
    
    def __str__(self):
        return "İsim:{} Rütbe:{} Güç:{} Puan:{}".format(self.isim,self.rutbe,self.guc,self.puan)
    
    #Destructor (Yıkıcı) metot
    #Nesneleri yok etme – Garbage collection
    def __del__(self):
        print("Yıkıcı metot çalıştı. Nesne silindi")
        class_name=self.__class__.__name__
        #class_name private bir değişkendir. 
        #Sadece bu metod içerisinde kullanılabilir.
        print(class_name,"yok edildi")
     
class Asker(Oyuncu):
    #chield (çocuk) class
    def __init__(self, isim, rutbe):
        super().__init__(isim,rutbe)
        self.guc=100
        self.puan=50
            
class Usta(Oyuncu):
    def __init__(self):
        #Geçersiz kılma (Overriding)
        self.guc=50
        self.puan=60
    
    def hareket_et(self):
        #Geçersiz kılma (Overriding)
        print("Hareket edildi")
        
    def __str__(self):
        return "Güç:{}".format(self.guc)

class Isci(Oyuncu):
    def __init__(self,*args):
        Oyuncu.__init__(self, *args)
        self.guc=75


isci=Isci("işçi",5)
isci.puan_kaybet(10)
print(isci.puan)



oyuncu=Oyuncu("oyuncu1",1)
print(oyuncu.guc)
print(oyuncu)

#oyuncu.__gizli=10
#Private değişkenler Class dışında değiştirilemez ve görüntülenemez
#Değiştirilebilmesi ve görüntülenmesi için Class içerisinde tanımlanmış metotlara ihtiyacımız vardır.

oyuncu.Get_gizli()

oyuncu.Set_gizli(5)
oyuncu.Get_gizli()

print(oyuncu._gizli)
oyuncu._gizli=2
print(oyuncu._gizli)


asker=Asker("asker",2)
print(asker.guc)
asker.puan_kazan(10)
print(asker.puan)
print(asker)

asker.Get_gizli()

asker2=Asker("asker2",3)
asker3=Asker("asker3",5)
print(id(asker),id(asker2),id(asker3))

asker4=asker
asker5=asker
print(id(asker),id(asker4),id(asker5))

del asker
del asker4
del asker5
#Nesneleri yok etme – Garbage collection (Çöp Toplama)
#Python’un periyodik olarak kullanımda olmayan bellek bloklarını sildiği süreçtir.
#Bir nesnenin referans sayısı sıfıra ulaştığında, Python otomatik olarak toplar.


usta=Usta()
usta.isim="usta"
usta.hareket_et()
print(usta)
usta.puan_kazan(10)

del usta
del oyuncu
