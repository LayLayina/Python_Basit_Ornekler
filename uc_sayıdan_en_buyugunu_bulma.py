print("""*****************************
Üç Adet Sayıdan En Büyüğünü Bulma Programı
Kasım Can Arslan
*****************************""")

sayı1 = float(input("Lütfen 1.Sayıyı Giriniz:"))
sayı2 = float(input("Lütfen 2.Sayıyı Giriniz:"))
sayı3 = float(input("Lütfen 3.Sayıyı Giriniz:"))

if (sayı1 >= sayı2 and sayı1 >= sayı3):
    print("En Büyük Sayı: {}".format(sayı1))

elif (sayı2 >= sayı1 and sayı2 >= sayı3):
    print("En Büyük Sayı: {}".format(sayı2))

elif (sayı3 >= sayı1 and sayı3 >= sayı2):
    print("En Büyük Sayı: {}".format(sayı3))