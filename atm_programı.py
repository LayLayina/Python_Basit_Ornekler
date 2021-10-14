print("""*********************************
Atm Programı
Kasım Can Arslan

İşlemler;
1.Bakiye Sorgulama
2.Para Yatırma
3.Para Çekme

Çıkmak İçin q ' ya Basınız.
*********************************""")

bakiye = 1000
sys_parola = "1234"



while True:
    parola = input("Lütfen Parolanızı Giriniz")

    if (sys_parola == parola):

        islem = input("Lütfen Yapmak İstediğiniz İşlemi Seçiniz:")

        if (islem == "q"):
            print("Yine Bekleriz.")
            break

        elif (islem == "1"):
            print("Bakiyeniz: {} TL ' dir.".format(bakiye))

        elif (islem == "2"):
            miktar = input("Lütfen Yatırmak İstediğniz Miktarı Giriniz:")
            bakiye += miktar
            print("Bakiyeniz: {} TL ' dir.".format(bakiye))

        elif (islem == "3"):
            miktar = input("Lütfen Çekmek İstediğiniz Miktarı Giriniz:")

            if (bakiye - miktar < 0):
                print("Yetersiz Bakiye")
                continue

            bakiye -= miktar

        else:
            print("Yine Bekleriz.")


    elif (sys_parola != parola):
        print("Şifreniz Yanlış Daha Sonra Tekrar Deneyiniz.")









