# -*- coding: utf-8 -*-
"""
Created on Mon Mar  9 11:07:07 2020

@author: gozdemihranaltinsoy
"""

#Kendisine gönderilen sayının faktöriyelini hesaplayan metod:
def faktoriyel(sayi):
    #5!=1*2*3*4*5=120
    #2!=1*2=2
    #0!=1
    #Negatif olduğunda "Tanımsız"
    if sayi<0:
        return "Tanımsız"
    sonuc=1
    for i in range(1,sayi+1):
        sonuc*=i #sonuc=sonuc*i
    return sonuc    
        
#Sayının karesini ekrana yazdıran metod:
def kare(sayi):
    try:
        return sayi*sayi  
    except:
        return "Hatalı giriş"
    
def kare2(sayi):
    if (sayi.isdigit()):
        #isdigit() string ile kullanılabilen bir fonksiyondur. 
        #str değer tamamen rakamlardan oluşuyorsa yani sayı ise True, değilse False değerini döndürür
        return int(sayi)*int(sayi)  
    else:
        return "Hatalı giriş"    
#Kendisine gönderilen sayı ve üs değerlerine göre üssünü hesaplayıp
#ekrana yazdıran metod:    
def us(sayi,us):        
    #pass  
    #Eğer bir bloğun içerisine bir şey yazmadan diğer koda geçmek isterseniz pass yazabilirsiniz.
    try:
        return sayi**us
    except:
        return "Hatalı işlem"
        
#Rastgele 1 ile 100 arasında üretilen 10 sayıyı ekrana yazdırıp, toplamlarını döndüren (return) metod:
def rastgele():        
    import random
    numbers=[]
    for i in range(1,11):
        numbers.append(random.randint(1,100))
    print(numbers)
    return sum(numbers)
    
#Klavyeden girilen iki sayının birbirine bölümünden kalanı ekrana yazdıran metod:
def mod():
    bolum=eval(input("Bölüm:"))
    #eval klavyeden girilen değer eğer tam sayı ise int, ondalıklı sayı ise float değişkende tutar
    bolen=eval(input("Bölen:"))
    print("Kalan:",bolum%bolen)
    
#Kendisine gönderilen değer kadar kendisine gönderilen
#min ve mak değerler arasında random değer üretip
#bu değerleri ana metoda döndüren metod:
#Parametre 3 değer, döndürülen random değerler (liste)
def sayi_uret(miktar,mini,maks):
    import random
    sayilar=[]
    if mini>maks:
        mini,maks=maks,mini
        #Eğer mini değeri maks değerinden büyük ise değişkenlerin içindeki değerleri yer değiştirdik
    """
    if miktar<0:
        miktar*=-1
        #Eğer miktar değeri negatif bir değer ise pozitif değere dönüştürdük
    """
    if miktar>0:
        for i in range(miktar):
            sayilar.append(random.randint(mini,maks))
    else:
        for i in range(0,miktar,-1):
            sayilar.append(random.randint(mini,maks))
    return sayilar    






    
    
    
    
    
        