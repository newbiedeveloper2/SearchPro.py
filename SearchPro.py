from tkinter import *
from tkinter.filedialog import askopenfilename
def arama():
    girdi=giris.get()
    bulunan=str(veri.count(girdi))
    sonuc.config(text=bulunan+" sonuç bulundu")
def aç():
    global veri
    global file
    file=askopenfilename()
    aç=open(file,'r',encoding = "utf8")
    veri=aç.read()
    aç.close()
    dosya=file.split("/")
    dosyaadı.config(text=dosya[-1])
def değiştirme():
    sonuc.config(text=str(veri.count(giris.get()))+" piece "+giris.get()+" -> "+giris2.get()+" replaced")
    yeniveri=veri.replace(giris.get(),giris2.get())
    global veri
    veri=yeniveri
def küçültme():
    yeniveri=veri
    büyük=["A","B","C","Ç","D","E","F","G","Ğ","H","I","İ","J","K","L","M","N","O","Ö","P","R","S","Ş","T","U","Ü","V","Y","Z","X","Q","W"]
    küçük=["a","b","c","ç","d","e","f","g","ğ","h","ı","i","j","k","l","m","n","o","ö","p","r","s","ş","t","u","ü","v","y","z","x","q","w"]
    for x,y in enumerate(büyük):
        yeniveri=yeniveri.replace(büyük[x],küçük[x])
    global veri
    veri=yeniveri
    sonuc.config(text="All Letters are LowerCase now")
def özelayar():
    yeniveri=veri
    sil=["%","$","^","<",">","|","?","=","*","(",")","[","]","{","}","/","@","~","^","?","£","ß","æ","Æ","!",":",";",".","`","€","à","–","�"]
    boşluk=["-","&","+",",","  "]
    for x,y in enumerate(sil):
        yeniveri=yeniveri.replace(sil[x],"")
    for a,b in enumerate(boşluk):
        yeniveri=yeniveri.replace(boşluk[a]," ")
    global veri
    veri=yeniveri
    sonuc.config(text="Made it compatible to SQL, Done!")
def kaydetme():
    aç=open(file,'w',encoding = "utf8")
    aç.write(veri)
    aç.close()
    sonuc.config(text="Saved")
pencere=Tk() 
pencere.geometry("200x300")
pencere.title("SearchPro")


yazi=Label(pencere)
yazi.config(text="Professional Search Tool")
yazi.pack()

dosya=Button(text="Open A File")
dosya.config(command=aç)
dosya.pack()

giris=Entry(pencere)
giris.pack()

ara=Button(text="Search")
ara.config(command=arama)
ara.pack()

giris2= Entry(pencere)
giris2.pack()

değiştir=Button(pencere)
değiştir.config(command=değiştirme,text="Replace")
değiştir.pack()

dosyaadı=Label(text="File couldn't opened!")
dosyaadı.pack()

küçült=Button(pencere)
küçült.config(text="LowerCase All letters",command=küçültme)
küçült.pack()

özel=Button(pencere)
özel.config(text="Make it compatible for SQL databases",command=özelayar)
özel.pack()

sonuc=Label()
sonuc.config(text="")
sonuc.pack()


kaydet=Button(pencere)
kaydet.config(command=kaydetme,text="Save")
kaydet.pack()

pencere.mainloop()
