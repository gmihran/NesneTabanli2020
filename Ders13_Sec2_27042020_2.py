# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 15:39:55 2020

@author: Gözde Mihran Altınsoy
"""
import tkinter

class Pencere(tkinter.Tk):
    def __init__(self):
        super().__init__()
        self.protocol("WM_DELETE_WINDOW",self.kapat)
        
        self.geometry("500x400")
        
        self.etiket=tkinter.Label(text="Merhaba Dünya",background="blue",foreground="white")
        self.etiket.pack()
        
        self.entry=tkinter.Entry()
        self.entry.pack()
        
        tkinter.Label(text="Bildiğiniz Diller")
        
        self.liste=tkinter.Listbox()
        self.liste.insert(1, "Python")
        self.liste.insert(2, "C++")
        self.liste.insert(3, "C#")
        self.liste.insert(4, "Java")
        self.liste.pack()
        
        tkinter.Label(text="Hobileriniz").pack()

        self.check1 = tkinter.Checkbutton(text="Spor yapmak",onvalue=1,offvalue=0)
        self.check1.pack()
        
        self.check2 = tkinter.Checkbutton(text="Kitap okumak",onvalue=1,offvalue=0)
        self.check2.pack()
        
        self.buton=tkinter.Button(text="Çıkış",command=self.kapat)
        self.buton.pack()
        
        self.mesajbuton=tkinter.Button(text="Mesaj ver",command=self.mesajver)
        self.mesajbuton.pack()
        
        self.labelsayi=tkinter.Label(text="1")
        self.labelsayi.pack()

        self.art=tkinter.Button(text="Arttır",command=self.arttir)
        self.art.pack()

        self.azal=tkinter.Button(text="Azalt",command=self.azalt)
        self.azal.pack()
    
    def mesajver(self):
        tkinter.messagebox.showinfo("Mesaj","Mesajınız var")
        
    
    def kapat(self):
        self.etiket["text"]="Güle güle"
        self.buton["text"]="Çıkış yapılıyor"
        self.buton["state"]="disabled"
        self.destroy()
        #self.after(1000, self.destroy)
        
    def arttir(self):
        #sayi=int(self.labelsayi["text"])
        #self.labelsayi["text"]=str(sayi+1)
        self.labelsayi["text"]=int(self.labelsayi["text"])+1
     
    def azalt(self):
        sayi=int(self.labelsayi["text"])
        self.labelsayi["text"]=sayi-1

pencere=Pencere()

pencere.mainloop()