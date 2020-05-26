# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 11:04:31 2020

@author: Gözde Mihran Altınsoy
"""

import tkinter

class Pencere(tkinter.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("500x500")
        self.protocol("WM_DELETE_WINDOW",self.Cikis)
        self.etiket=tkinter.Label(text="Merhaba",background="black",foreground="white")
        self.etiket.pack()
        
        
        self.entry1=tkinter.Entry()
        self.entry1.pack()
        
        self.etiket1=tkinter.Label(text="Bildiğiniz Diller")
        self.etiket1.pack()
        
        self.liste=tkinter.Listbox()
        self.liste.insert(1, "Python")
        self.liste.insert(2, "C++")
        self.liste.insert(3, "C#")
        self.liste.insert(4, "VBA")
        self.liste.pack()
        
        self.etiket2=tkinter.Label(text="Hobileriniz")
        self.etiket2.pack()
        
        self.check1=tkinter.Checkbutton(text="Spor yapmak",onvalue=1,offvalue=0)
        self.check1.pack()
        
        self.check2=tkinter.Checkbutton(text="Kitap okumak",onvalue=1,offvalue=0)
        self.check2.pack()
        
        self.dugme=tkinter.Button(text="Çıkış",command=self.Cikis)
        self.dugme.pack()
        self.mesajdugmesi=tkinter.Button(text="Mesaj ver",command=self.mesajver)
        self.mesajdugmesi.pack()
        
    
    def Cikis(self):
        self.etiket["text"]="Güle güle"
        self.dugme["text"]="Çıkış yapılıyor"
        self.dugme["state"]="disabled"
        self.after(2000,self.destroy)
    
    def mesajver(self):
        tkinter.messagebox.showinfo("Mesaj","Mesajınız var")
        
pencere=Pencere()


pencere.mainloop()

#pencere2=Pencere()

#pencere2.mainloop()

    
    
    
