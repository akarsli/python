# İnsan sınıfı (temel sınıf)
class Insan:
    def __init__(self, ad, yas):
        self.ad = ad
        self.yas = yas

    def konus(self):
        print(f"Merhaba, ben {self.ad}. Güzel bir gün değil mi?")


# Hoca sınıfı (İnsan sınıfından miras alıyor)
class Hoca(Insan):
    def __init__(self, ad, yas, sicil_no):
        super().__init__(ad, yas)
        self.sicil_no = sicil_no

    def konus(self):
        print(f"Ben Hoca {self.ad}. Dersi dikkatli dinleyin!")

    def ders_ver(self):
        print(f"Hoca {self.ad} şu anda ders veriyor.")


# Sekreter sınıfı (İnsan sınıfından miras alıyor)
class Sekreter(Insan):
    def __init__(self, ad, yas, departman):
        super().__init__(ad, yas)
        self.departman = departman

    def konus(self):
        print(f"Ben {self.ad}, {self.departman} departmanında sekreterim.")

    def randevu_ayarla(self):
        print(f"Sekreter {self.ad} yeni bir randevu ayarlıyor.")


# Öğrenci sınıfı (İnsan sınıfından miras alıyor)
class Ogrenci(Insan):
    def __init__(self, ad, yas, ogrenci_no):
        super().__init__(ad, yas)
        self.ogrenci_no = ogrenci_no

    def konus(self):
        print(f"Ben öğrenci {self.ad}, derse geç kalmayayım!")

    def ders_calıs(self):
        print(f"Öğrenci {self.ad} şu anda ders çalışıyor.")


# Örnek kullanım:
if __name__ == "__main__":
    insan = Insan("Ahmet", 40)
    hoca = Hoca("Ayşe", 35, "H123")
    sekreter = Sekreter("Fatma", 28, "Bilgisayar Mühendisliği")
    ogrenci = Ogrenci("Mehmet", 21, "2025001")

    insan.konus()
    hoca.konus()
    hoca.ders_ver()
    sekreter.konus()
    sekreter.randevu_ayarla()
    ogrenci.konus()
    ogrenci.ders_calıs()
