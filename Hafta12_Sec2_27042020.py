# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 15:06:24 2020

@author: Gözde Mihran Altınsoy
"""

import tkinter
pencere=tkinter.Tk() #nesne (obje,örnek) oluşturuldu
pencere.geometry('500x400') #tek tırnak ve çift tırnak kullanılabilir


def kapat():
    etiket["text"]="Güle güle"
    dugme["text"]="Çıkış yapılıyor"
    dugme["state"]="disabled"
    pencere.destroy()
    #pencere.after(2000, pencere.destroy)

def mesajver():
    tkinter.messagebox.showinfo("Mesaj","Mesajınız var")
 
def arttir():
    #sayi=int(labelsayi["text"])
    #labelsayi["text"]=str(sayi+1)
    labelsayi["text"]=int(labelsayi["text"])+1
     
def azalt():
    sayi=int(labelsayi["text"])
    labelsayi["text"]=sayi-1

pencere.protocol("WM_DELETE_WINDOW",kapat)

etiket=tkinter.Label(text="Merhaba Dünya")
etiket.pack()

entry=tkinter.Entry()
entry.pack()

tkinter.Label(text="Bildiğiniz Diller")
liste=tkinter.Listbox()
liste.insert(1, "Python")
liste.insert(2, "C++")
liste.insert(3, "C#")
liste.insert(4, "Java")
liste.pack()

tkinter.Label(text="Hobileriniz").pack()

check1 = tkinter.Checkbutton(text="Spor yapmak",onvalue=1,offvalue=0)
check1.pack()

check2 = tkinter.Checkbutton(text="Kitap okumak",onvalue=1,offvalue=0)
check2.pack()


#dugme=tkinter.Button(text="Çıkış",command=pencere.destroy)
dugme=tkinter.Button(text="Çıkış",command=kapat)
dugme.pack()

mesajbuton=tkinter.Button(text="Mesaj ver",command=mesajver)
mesajbuton.pack()

labelsayi=tkinter.Label(text="1")
labelsayi.pack()

art=tkinter.Button(text="Arttır",command=arttir)
art.pack()

azal=tkinter.Button(text="Azalt",command=azalt)
azal.pack()

pencere.mainloop()
