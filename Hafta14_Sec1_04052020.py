# -*- coding: utf-8 -*-
"""
Created on Mon May  4 10:16:32 2020

@author: Gözde Mihran Altınsoy
"""

import sqlite3
con=sqlite3.connect("kullanici.db")
cursor=con.cursor()

def tabloolustur():
    cursor.execute("CREATE TABLE IF NOT EXISTS kullanicigiris(kullaniciadi TEXT, sifre TEXT)")
    cursor.execute("CREATE TABLE IF NOT EXISTS kullanicidetay(kullaniciadi TEXT, adi TEXT, soyadi TEXT, ogrenci INT, medeni TEXT)")
    con.commit()
    
    
def kayitolustur(kadi,sifre):
    cursor.execute("SELECT kullaniciadi FROM kullanicigiris WHERE kullaniciadi=?",(kadi,))
    veri=cursor.fetchall()
    print(veri)
    if len(veri)==0:
        cursor.execute("INSERT INTO kullanicigiris VALUES(?,?)",(kadi,sifre))
        con.commit()
        messagebox.showinfo("Durum","Kayıt başarılı")
    else:
        messagebox.showinfo("Hata","Kullanıcı bilgileri geçersiz")
    

def girisdene(kadi,sifre):
    cursor.execute("SELECT kullaniciadi FROM kullanicigiris WHERE kullaniciadi=? AND sifre=?",(kadi,sifre))
    veri=cursor.fetchall()
    if len(veri)==1:
        messagebox.showinfo("Giriş Durumu","Giriş başarılı")
        return True
    else:
        messagebox.showinfo("Giriş Durumu","Giriş başarısız")
        return False
    

def detayolustur(kadi,adim,soyadim,ogrencidurumum,medenidurumum):
    #kullanicidetay(kullaniciadi TEXT, adi TEXT, soyadi TEXT, ogrenci INT, medeni TEXT
    cursor.execute("SELECT kullaniciadi FROM kullanicidetay WHERE kullaniciadi=?",(kadi,))
    veri=cursor.fetchall()
    if len(veri)==0:
        cursor.execute("INSERT INTO kullanicidetay VALUES(?,?,?,?,?)",(kadi,adim,soyadim,ogrencidurumum,medenidurumum))
        con.commit()
    else:
        cursor.execute("UPDATE kullanicidetay SET adi=?,soyadi=?,ogrenci=?,medeni=? WHERE kullaniciadi=?",(adim,soyadim,ogrencidurumum,medenidurumum,kadi))
        con.commit()

tabloolustur()

from tkinter import *
from tkinter import messagebox

class KullaniciKayit(Tk):
    def __init__(self):
        #yapıcı
        super().__init__()
        #super ile Tk class'ına ait olan tüm özellikleri miras aldık
        self.geometry("200x130")
        
        Label(text="Kullanıcı Adı").grid(row=0,column=0)
        
        self.kadi=Entry()
        self.kadi.grid(row=0,column=1)
        
        Label(text="Şifre").grid(row=1,column=0)
        
        self.sifre=Entry()
        self.sifre.grid(row=1,column=1)

        Label(text="Şifre Tekrar").grid(row=2,column=0)
        
        self.sifretekrar=Entry()
        self.sifretekrar.grid(row=2,column=1)
        
        self.giris=Button(text="Kayıt ol",command=self.kaydet)
        self.giris.grid(row=3,column=0,columnspan=2)
        
    def kaydet(self):
        #print(self.kadi.get())
        kadim=self.kadi.get()
        sifrem=self.sifre.get()
        sifremtekrar=self.sifretekrar.get()
        if (kadim!="" and sifrem!="" and sifrem==sifremtekrar):
            kayitolustur(kadim,sifrem)
        elif sifrem!=sifremtekrar:
            messagebox.showinfo("Durum","Kayıt başarısız. Şifreler uyuşmuyor")
        else:
            messagebox.showinfo("Durum","Kayıt başarısız. Değerler boş geçilemez")
        
        
class KullaniciGiris(Tk):
    def __init__(self):
        super().__init__()
        self.geometry("200x130")
        
        Label(text="Kullanıcı Adı").grid(row=0,column=0)
        
        self.kadi=Entry()
        self.kadi.grid(row=0,column=1)
        
        Label(text="Şifre").grid(row=1,column=0)
        
        self.sifre=Entry()
        self.sifre.grid(row=1,column=1)
        
        self.giris=Button(text="Giriş yap",command=self.girisyap)
        self.giris.grid(row=2,column=0,columnspan=2)
        
    def girisyap(self):
        global oturum
        oturum=self.kadi.get()
        sifrem=self.sifre.get()
        if oturum!="" and sifrem!="":
            self.durum=girisdene(oturum,sifrem)
        else:
            self.durum=False
            messagebox.showinfo("Hata","Değerler boş geçilemez")
        if (self.durum):
            self.destroy()
            pencere=Pencere()
            pencere.mainloop()
            
class Pencere(Tk):
    def __init__(self):
        super().__init__()
        
        self.geometry("500x500")
        
        Label(text="Kullanıcı Adı").grid(row=0,column=0)
        #Kontrol yaptık
        #global oturum
        #oturum="gozde2"
        self.kadi=Label(text=oturum)
        self.kadi.grid(row=0,column=1)
        
        Label(text="Adı").grid(row=1,column=0)
        
        self.adi=Entry()
        self.adi.grid(row=1,column=1)
        
        Label(text="Soyadi").grid(row=2,column=0)
        
        self.soyadi=Entry()
        self.soyadi.grid(row=2,column=1)
        
        Label(text="Öğrencilik Durumu").grid(row=3,column=0)
        
        self.ogrenci=IntVar()
        self.checkogrenci=Checkbutton(text="Aktif/Pasif",variable=self.ogrenci,onvalue=1,offvalue=0)
        self.checkogrenci.grid(row=3,column=1)
        
        Label(text="Medeni Durumu").grid(row=4,column=0,rowspan=2)
        
        self.medenidurum=StringVar()
        self.radiomedenidurum1=Radiobutton(text="Evli",variable=self.medenidurum,value="Evli")
        self.radiomedenidurum1.grid(row=4,column=1)
        self.radiomedenidurum1.select()
        
        self.radiomedenidurum2=Radiobutton(text="Bekar",variable=self.medenidurum,value="Bekar")
        self.radiomedenidurum2.grid(row=5,column=1)
        
        
        self.kaydet=Button(text="Kaydet",command=self.kayitolustur)
        self.kaydet.grid(row=6,column=0,columnspan=2)
    
    def kayitolustur(self):
        
        #print(self.ogrenci.get(),self.medenidurum.get())
        adim=self.adi.get()
        soyadim=self.soyadi.get()
        ogrencidurumum=self.ogrenci.get()
        medenidurumum=self.medenidurum.get()
        if adim!="" and soyadim!="":
            detayolustur(oturum,adim,soyadim,ogrencidurumum,medenidurumum)
    
"""        
kullanicikayit=KullaniciKayit()
kullanicikayit.mainloop()
"""

kullanicigiris=KullaniciGiris()
kullanicigiris.mainloop()

#kullanicipencere=Pencere()
#kullanicipencere.mainloop()

con.close()


