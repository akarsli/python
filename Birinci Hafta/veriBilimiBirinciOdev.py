print("Abdulkadir Karslı")

print("---------")

a="ali"
b=5

print(type(a))
print(type(b))

a.capitalize()

print("---------")

""""Yorum Satırı"""

liste=[1,2,4,3,5,6]
liste.sort()
print(liste)

print("---------")

def selam():
    print("Selam")

selam()

print("---------")

def topla(a,b):
    c=a+b
    print(c)

topla(1,5)

print("---------")
    

class araba():
    renk="sarı"
    model="Tiguan"
    marka="VW"

a1=araba()

print(a1.renk)
print(a1.marka)
print(a1.model)

print("---------")

class isci():
    
    yas=20
    maas=3000

    def yasaGoreMaasOranla(self):
        print(self.yas/self.maas)

isci1=isci()

isci1.yasaGoreMaasOranla()

print("---------")

class Animal():
    def __init__(self):
        print("hayvan sınıfının yapıcı metotum")
    def sesCikar(self):
        print("hav,miyav,vak....")
    def hareket(self):
        print("zıplar,koşar,yürür..")

class kedi(Animal):
    def __init__(self):
        super().__init__() # yazmasakta olur ata sınıfın init metodunu ezeriz metot overriding!!
        print("kedi sınıfı oluşturuldu")
    def sesCikar(self):
        print("miyav")
    def DokuzCan(self): #diğer hayvanlardan ayrılan bir fonksiyon :D
        print("Bu sevimli hayvanlar hep dört ayak üstüne düşer")

k1=kedi()
k1.sesCikar() #ata sınıfı ezer
k1.hareket()
k1.DokuzCan()

print("---------")

class Animal():
    def sesVer(self):
        print("ses çıkarırlar")
class kedi(Animal):
    def sesVer(self): #ata sınıfı ezdi
        print("miyav")
a=Animal()
a.sesVer()
k=kedi()
k.sesVer()