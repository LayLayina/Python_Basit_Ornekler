print("""***************************************
Üçgen Kare Bulma Algoritma Programı 
Kasım Can Arslan
***************************************""")



print("\n1.Üçgen \n2.Dörtgen")
sekil = input("Lütfen Bulmak İstediğiniz Şekli Seçiniz;")


if (sekil == "dörtgen"):
    dörtgen_1_kenar = float(input("Lütfen Dörtgenin 1.Kenarının Uzunluğunu Giriniz:"))
    dörtgen_2_kenar = float(input("Lütfen Dörtgenin 2.Kenarının Uzunluğunu Giriniz:"))
    dörtgen_3_kenar = float(input("Lütfen Dörtgenin 3.Kenarının Uzunluğunu Giriniz:"))
    dörtgen_4_kenar = float(input("Lütfen Dörtgenin 4.Kenarının Uzunluğunu Giriniz:"))

    if (dörtgen_1_kenar == dörtgen_2_kenar and dörtgen_1_kenar == dörtgen_3_kenar and dörtgen_1_kenar == dörtgen_4_kenar):
        print("Şekliniz Kare'dir")

    elif (dörtgen_1_kenar == dörtgen_3_kenar and dörtgen_2_kenar == dörtgen_4_kenar):
        print("Şekliniz Dikdörtgen'dir")

    else:
        print("Şekliniz Dörtgen'dir")


elif (sekil == "üçgen"):
    ücgen_1_kenar = float(input("Lütfen Üçgeninizin 1.Kenarının Uzunluğunu Giriniz:"))
    ücgen_2_kenar = float(input("Lütfen Üçgeninizin 2.Kenarının Uzunluğunu Giriniz:"))
    ücgen_3_kenar = float(input("Lütfen Üçgeninizin Taban Uzunluğunu Giriniz:"))

    if (abs(ücgen_1_kenar + ücgen_2_kenar) > ücgen_3_kenar and abs(ücgen_1_kenar + ücgen_3_kenar) > ücgen_2_kenar and abs(ücgen_3_kenar + ücgen_2_kenar) > ücgen_1_kenar):

         if (ücgen_1_kenar == ücgen_2_kenar and ücgen_1_kenar == ücgen_3_kenar):
             print("Eşkenar Üçgen")

         elif ((ücgen_1_kenar == ücgen_2_kenar and ücgen_1_kenar != ücgen_3_kenar) or (ücgen_1_kenar == ücgen_3_kenar and ücgen_1_kenar != ücgen_2_kenar) or (ücgen_2_kenar == ücgen_3_kenar and ücgen_2_kenar != ücgen_1_kenar)):
             print("İkizkenar Üçgen")

         else:
             print("Çesitkenar Üçgen")

    else:
        print("Üçgen Belirtmiyor")

else:
    print("Gçersiz Şekil")




