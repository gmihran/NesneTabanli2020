# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 09:54:43 2020

@author: Gözde Mihran Altınsoy
"""

import tkinter
from tkinter import messagebox
pencere=tkinter.Tk()
#pencere diye Tk Class'ından nesne(obje,örnek) oluşturuldu.

def cikis():
    etiket["text"]="Güle güle"
    dugme["text"]="Çıkış yapılıyor"
    dugme["state"]="disabled"
    #dugme objesinin pasif olmasını sağlar. Böylece kullanıcı bir daha düğmeye tıklayamaz
    pencere.destroy()
    #pencere.after(2000, pencere.destroy)
    #2000 ms (2 sn) bekler, sonrasında pencereyi kapatır

def mesajver():
    messagebox.showinfo("Uyarı","Mesajınız var")

def arttir():
    global s
    s=int(sayi["text"])
    sayi["text"]=str(s+1)
    
def azalt():
    global s
    s=int(sayi["text"])
    sayi["text"]=str(s-1)
    

pencere.geometry("500x500")

etiket=tkinter.Label(text="Merhaba Dünya")
etiket.pack()

entry1=tkinter.Entry()
entry1.pack()

etiket1=tkinter.Label(text="Bildiğiniz Diller")
etiket1.pack()

liste=tkinter.Listbox()
liste.insert(1, "Python")
liste.insert(2, "C++")
liste.insert(3, "C#")
liste.insert(4, "VBA")
liste.pack()

etiket2=tkinter.Label(text="Hobileriniz")
etiket2.pack()

check1=tkinter.Checkbutton(text="Spor yapmak",onvalue=1,offvalue=0)
check1.pack()

check2=tkinter.Checkbutton(text="Kitap okumak",onvalue=1,offvalue=0)
check2.pack()


#dugme=tkinter.Button(text="Çıkış",command=pencere.destroy)

dugme=tkinter.Button(text="Çıkış",command=cikis)
dugme.pack()

mesajbutton=tkinter.Button(text="Mesaj ver",command=mesajver)
mesajbutton.pack()

pencere.protocol("WM_DELETE_WINDOW",cikis)

sayi=tkinter.Label(text="1")
sayi.pack()

art=tkinter.Button(text="Arttır",command=arttir)
art.pack()

azal=tkinter.Button(text="Azalt",command=azalt)
azal.pack()

pencere.mainloop()
#Pencerenin ekranda görünmesini sağlar