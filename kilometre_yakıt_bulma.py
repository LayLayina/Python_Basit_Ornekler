print("""---------------------------
Toplam Ödenecek Akaryakıt Fiyat Hesaplama Programı
Kasım Can Arslan
---------------------------""")

print("Güncel Benzin Fiyatı: 7,13 ")

yaktığı_miktar = float(input("Aracınızın Kilometrede Ne Kadar Yaktığını Giriniz:"))
km = int(input("Kaç Kilometre Yol Yaptığınızı Giriniz:"))
i = 7.13

fiyat = yaktığı_miktar * km
fiyat2 = fiyat * i



print(fiyat2 , "TL")

