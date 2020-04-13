# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 09:58:41 2020

@author: Gözde Mihran Altınsoy
"""

#class'ların ilk harfi büyük harf olmalıdır.
class Bilgisayar:
    def __init__(self,guc):
        #constructor (yapıcı)
        self.guc=guc
        #Attribute (nitelik,özellik)
    

#Bilgisayar Parçaları
#Inheritance (miras alma, kalıtım)
class Minibilgisayar(Bilgisayar): #Child (çocuk)
    
    def __init__(self,guc=165): #self Hangi nesneyi referans gösterdiğini ifade eder
    #constructor (yapıcı)
        print("Yapıcı çalıştı")
        if guc>0:
            self.guc=guc
        else:
            self.guc=165
            print("Güç değeri atanamadı. Çünkü güç değeri negatif değer olamaz.")
        
    def GetGuc(self):
        return self.guc
    
    def GetGuc2(self):
        print("Güç:",self.guc)
        
    def SetGuc(self,gucu):
        self.guc=gucu
        
    def SetGetGuc(self,gucu):
        self.guc=gucu
        return self.guc

    
class Dizustubilgisayar(Bilgisayar):
    
    def __init__(self,guc=250,ekranboyut=14,ekranhiz=60,gecikmesuresi=1):
        #constructor (yapıcı)
        self.guc=guc
        self.ekranboyut=ekranboyut
        self.ekranhiz=ekranhiz
        self.gecikmesuresi=gecikmesuresi
    def __str__(self):
        #Geri döndürülen değer string türünde olmalıdır.
        return "Güç:{}\nEkran boyutu:{}\nEkran hızı:{}\nGecikme süreci:{}".format(self.guc,self.ekranboyut,self.ekranhiz,self.gecikmesuresi)
        
#class Ekran(Dizustubilgisayar(Bilgisayar)):
#      pass

class Masaustubilgisayar(Bilgisayar):
    pass

laptop=Dizustubilgisayar()
#<__main__.Dizustubilgisayar object at 0x0000016EA6C4E348>
print(laptop)
print()

laptop.ekranboyut=17
laptop.ekranhiz=80
laptop.gecikmesuresi=0.5

print(laptop)


print()
#Nesne = Örnek (aynı anlama gelir.)
minibilgisayar=Minibilgisayar() #minibilgisayar nesnesi (örneği? türetildi (Minibilgisayar class'ından)
print(minibilgisayar.guc)
print(minibilgisayar.GetGuc())

minibilgisayar.guc=180
minibilgisayar.GetGuc2()

minibilgisayar.SetGuc(225)
minibilgisayar.GetGuc2()


minibilgisayar.marka="x"
print(minibilgisayar.marka)

#print(minibilgisayar.ekranboyut)
#Eğer nitelik tanımlanmadıysa veya burada bu niteliğe ait bir değer ataması gerçekleştirmezse bu nitelik ile ilgili işlemler yapamayız.
#AttributeError: 'Minibilgisayar' object has no attribute 'ekranboyut'


minibilgisayar.ekranboyut=5
print(minibilgisayar.ekranboyut)


print("Güç:",minibilgisayar.SetGetGuc(230))

minibilgisayar2=Minibilgisayar(200) #minibilgisayar2 nesnesi (örneği) türetildi (Minibilgisayar class'ından)
print(minibilgisayar2.guc)

print()
mini=Minibilgisayar(-10)
mini.GetGuc2()


