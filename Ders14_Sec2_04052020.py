# -*- coding: utf-8 -*-
"""
Created on Mon May  4 15:00:39 2020

@author: Gözde Mihran Altınsoy
"""

import sqlite3
con=sqlite3.connect("kullanicibilgi.db")
cursor=con.cursor()

def tabloolustur():
    cursor.execute("CREATE TABLE IF NOT EXISTS kullanicigiris(kullaniciadi TEXT,sifre TEXT)")
    cursor.execute("CREATE TABLE IF NOT EXISTS kullanicidetay(kullaniciadi TEXT,adi TEXT, soyadi TEXT, ogrenci INT, medeni TEXT)")
    con.commit()
    
def kaydet(kadi,sifre):
    cursor.execute("SELECT kullaniciadi FROM kullanicigiris WHERE kullaniciadi=?",(kadi,))
    veri=cursor.fetchall()
    if len(veri)==0:
        cursor.execute("INSERT INTO kullanicigiris VALUES(?,?)",(kadi,sifre))
        messagebox.showinfo("Durum","Kayıt başarılı")
    else:
        messagebox.showinfo("Hata","Kayıt başarısız. Bu kullanıcı adı kullanımdadır")
    con.commit()
    
def kullanicigirisyap(kadi,sifre):
    cursor.execute("SELECT kullaniciadi FROM kullanicigiris WHERE kullaniciadi=? AND sifre=?",(kadi,sifre))
    veri=cursor.fetchall()
    print(veri)
    if len(veri)==1:
        messagebox.showinfo("Durum","Giriş başarılı")
        return True
    else:
        messagebox.showinfo("Durum","Giriş başarısız")
        return False
        
        
def verilerikaydet(kadi,adim,soyadim,ogrencidurumum,medenidurumum):
    cursor.execute("SELECT kullaniciadi FROM kullanicidetay WHERE kullaniciadi=?",(kadi,))
    veri=cursor.fetchall()
    print(veri)
    if len(veri)==0:
        cursor.execute("INSERT INTO kullanicidetay VALUES(?,?,?,?,?)",(kadi,adim,soyadim,ogrencidurumum,medenidurumum))
        con.commit()
        messagebox.showinfo("Durum","Kayıt başarılı")
    else:
        cursor.execute("UPDATE kullanicidetay SET adi=?,soyadi=?,ogrenci=?,medeni=? WHERE kullaniciadi=?",(adim,soyadim,ogrencidurumum,medenidurumum,kadi))
        con.commit()
        messagebox.showinfo("Durum","Kayıt güncellendi")
        
    
from tkinter import *
from tkinter import messagebox

class KullaniciKayit(Tk):
    def __init__(self):
        super().__init__()
        
        self.geometry("200x130")
        
        Label(text="Kullanıcı Adı:").grid(row=0,column=0)
        
        self.kadi=Entry()
        self.kadi.grid(row=0,column=1)
        
        Label(text="Şifre:").grid(row=1,column=0)
        
        self.sifre=Entry()
        self.sifre.grid(row=1,column=1)
        
        Label(text="Şifre tekrar:").grid(row=2,column=0)
        
        self.sifretekrar=Entry()
        self.sifretekrar.grid(row=2,column=1)
        
        self.kayit=Button(text="Kayıt ol",command=self.kayitol)
        self.kayit.grid(row=3,column=0,columnspan=2)
        
    def kayitol(self):
        kadim=self.kadi.get()
        sifrem=self.sifre.get()
        sifretekrarim=self.sifretekrar.get()
        if kadim!="" and sifrem!="" and sifrem==sifretekrarim:
            kaydet(kadim,sifrem)
        elif sifrem!=sifretekrarim:
            messagebox.showinfo("Durum","Kayıt başarısız. Şifreler uyuşmuyor")
        else:
            messagebox.showinfo("Durum","Kayıt başarısız. Değerler boş geçilemez")
        
    

class KullaniciGiris(Tk):
    def __init__(self):
        super().__init__()
        
        self.geometry("200x130")
        
        Label(text="Kullanıcı Adı:").grid(row=0,column=0)
        
        self.kadi=Entry()
        self.kadi.grid(row=0,column=1)
        
        Label(text="Şifre:").grid(row=1,column=0)
        
        self.sifre=Entry()
        self.sifre.grid(row=1,column=1)
        
        
        self.kayit=Button(text="Giriş yap",command=self.girisyap)
        self.kayit.grid(row=2,column=0,columnspan=2)
        
    def girisyap(self):
        global kadim
        kadim=self.kadi.get()
        sifrem=self.sifre.get()
        if kadim!="" and sifrem!="":
            durum=kullanicigirisyap(kadim,sifrem)
        if durum:
            self.destroy()
            pencere=Pencere()
            pencere.mainloop()

class Pencere(Tk):
    def __init__(self):
        super().__init__()
        
        self.geometry("300x300")
        
        Label(text="Kullanıcı Adı").grid(row=0,column=0)
        
        self.kadi=Label(text=kadim)
        self.kadi.grid(row=0,column=1)
        
        Label(text="Adı").grid(row=1,column=0)
        
        self.adi=Entry()
        self.adi.grid(row=1,column=1)
        
        Label(text="Soyadı").grid(row=2,column=0)
        
        self.soyadi=Entry()
        self.soyadi.grid(row=2,column=1)
        
        Label(text="Öğrencilik Durumu").grid(row=3,column=0)
        
        self.ogrenci=IntVar()
        self.checkogrenci=Checkbutton(text="Aktif/Pasif",variable=self.ogrenci,onvalue=1,offvalue=0)
        self.checkogrenci.grid(row=3,column=1)
        
        Label(text="Medeni Durumu").grid(row=4,column=0,rowspan=2)

        self.medeni=StringVar()
        self.radiomedeni=Radiobutton(text="Evli",variable=self.medeni,value="Evli")  
        self.radiomedeni.grid(row=4,column=1)
        self.radiomedeni.select()
        
        self.radiomedeni2=Radiobutton(text="Bekar",variable=self.medeni,value="Bekar")
        self.radiomedeni2.grid(row=5,column=1)
        
        self.kaydet=Button(text="Kaydet",command=self.kayityap)
        self.kaydet.grid(row=6,column=0,columnspan=2)
        
    def kayityap(self):
        #print(self.ogrenci.get(),self.medeni.get())
        adim=self.adi.get()
        soyadim=self.soyadi.get()
        ogrencidurumum=self.ogrenci.get()
        medenidurumum=self.medeni.get()
        if adim!="" and soyadim!="":
            verilerikaydet(kadim,adim,soyadim,ogrencidurumum,medenidurumum)
        
tabloolustur() 
  
"""
kullanicikayit=KullaniciKayit()
kullanicikayit.mainloop()
"""
kullanicigiris=KullaniciGiris()
kullanicigiris.mainloop()

#pencere=Pencere()
#pencere.mainloop()


con.close()
