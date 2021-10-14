#Bu projede ise 4 tane sınıfı oluşturun.
#Hayvan Sınıfı ------> Bütün hayvanların ortak özelliklerinin toplandığı sınıf olacak.
#Köpek Sınıfı ------> Bu sınıf, hayvan sınıfından miras alan bir sınıf olacak. Ayrıca bu sınıfa köpeklere ait ek özellikler ve metodlar ekleyin.
#Kuş Sınıfı ------> Bu sınıf, hayvan sınıfından miras alan bir sınıf olacak. Ayrıca bu sınıfa kuşlara ait ek özellikler ve metodlar ekleyin.
#At Sınıfı ------> Bu sınıf, hayvan sınıfından miras alan bir sınıf olacak. Ayrıca bu sınıfa atlara ait ek özellikler ve metodlar ekleyin.



class hayvan():
    def __init__(self,renk = "Belirtilmedi",yas = 0):
        self.renk = renk
        self.yas = yas

    def bilgileri_gösterme(self):
        print("Renk: {} \nYaş: {}".format(self.renk,self.yas))

    def renk_ekle_cıkar(self):
        renk_islem = input("Renk Eklemek İçin + Çıkarmak için - Çıkmak İçin q basınız.")
        if renk_islem == "+":
            giris_renk = input("Eklemek İstediğiniz Rengi Giriniz:")
            self.renk.append(giris_renk)
            print("Güncel Renkler: {}".format)


class köpek():
    pass

class kus():
    pass

class at():
    pass