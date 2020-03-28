# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 16:34:01 2020

@author: Gözde Mihran Altınsoy

Bu modülde sözlüklerle ilgili işlemler yapılacaktır.
"""

personel={"isim":"Gözde","soyisim":"Altınsoy","ünvan":"Öğretim Görevlisi"}

print(personel["isim"])
print(personel["ünvan"])

print(personel)

personel["yaş"]=33
print(personel["yaş"])
print(personel)

print(personel.keys())
print(personel.values())

print(personel.get("isim"))
#get ile köşeli parantez kullanarak değer getirme işlemindeki fark nedir?
#get() fonksiyonun farkı , anahtar bulunamazsa KeyError yerine None döndürmesidir.
print(personel["isim"])

print(personel.get("şehir"))
#None değeri döndürülür

#print(personel["şehir"])
#Bu anahtar bulunmadığı için KeyError hatası döndürür

try:
    #a=10+"a"
    print(personel["şehir"])   
except KeyError:
    #Hataya özel mesaj oluşturduk
    print("Anahtar bulunamadı")
except:
    print("Bilinmeyen bir hata oluştu")