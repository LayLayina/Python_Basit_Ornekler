print(""" ------------------------------
Oyuncu Kaydetme programı
Kasım Can Arslan
-----------------------------------------""")
ad = input("Lütfen İsminizi Giriniz:")

try:
    yas = int(input("Lütfen Yaşınızı Giriniz:"))
    print(yas)
except ValueError:
    print("Lütfen Yaşınızı Sayı Biçiminde Yazınız.")

yas = int(input("Lütfen Yaşınızı Giriniz:"))
okul = input("Lütfen Eğitim Durumunuzu Giriniz:")

bilgiler = [ad,yas,okul]

print("\n\nTebrikler Başarıyla Kaydınız Yapılmıştır.Bilgileriniz Aşagıda Görülmektedir.")
print("Oyuncunun Adı: {} \nOyuncunun Yaşı: {} \nOyuncunun Eğitim Durumu: {}".format(bilgiler[0],bilgiler[1],bilgiler[2]) )