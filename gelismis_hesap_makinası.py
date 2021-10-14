print("""------------------------------------
Kasım Can Arslan
Modül Kullanarak Gelişmiş Hesap Makinası Projesi
------------------------------------
İşlemler;
1-Toplama
2-Çıkarma
3-Çarpma
4-Bölme
5-Bölümden Kalan Bulma #math.fmod
6-Üs Bulma
7-Faktöriyel Bulma
8-EBOB Bulma #math.gcd
9-KareKök Bulma #math.sqrt
10-Mutlak Değer Bulma
""")


import math

while True:
    islem = input("İşlem Seçiniz:")

    if (islem == "1"):
        toplanacak1 = int(input("Toplanacak 1.Sayıyı Giriniz:"))
        toplanacak2 = int(input("Toplanacak 2.Sayıyı Giriniz:"))
        print("Toplam:", toplanacak1 + toplanacak2)

    elif (islem == "2"):
        cıkarma1 = int(input("Çıkaralacak 1.Sayıyı Giriniz:"))
        cıkarma2 = int(input("Çıkaralacak 2.Sayıyı Giriniz:"))
        print("Sonuç:", cıkarma1 - cıkarma2)

    elif (islem == "3"):
        carpma1 = int(input("Çarpılacak 1.Sayıyı Giriniz:"))
        carpma2 = int(input("Çarpılacak 2.Sayıyı Giriniz:"))
        print("Sonuç:", carpma1 * carpma2)

    elif (islem == "4"):
        bölen1 = int(input("Bölünelecek Sayıyı Giriniz:"))
        bölen2 = int(input("Bölecek Sayıyı Giriniz:"))
        print("Sonuç:", bölen1 / bölen2)

    elif (islem == "5"):
        bölünecek1 = int(input("Bölünelecek Sayıyı Giriniz:"))
        bölünecek2 = int(input("Bölecek Sayıyı Giriniz:"))
        kalan = math.fmod(bölünecek1, bölünecek2)
        print(kalan)

    elif (islem == "6"):
        alt = int(input("Alt Sayıyı Giriniz:"))
        üst = int(input("Üst Sayıyı Giriniz:"))
        sayı = alt ** üst
        print("Sonuç:", sayı)

    elif (islem == "7"):
        x = int(input("Faktöriyel Sayı Giriniz:"))
        fak = math.factorial(x)
        print("Sonuç:", fak)

    elif (islem == "8"):
        ebob1 = int(input("1.Sayıyı Giriniz:"))
        ebob2 = int(input("2.Sayıyı Giriniz:"))
        y = math.gcd(ebob1 , ebob2)
        print("Sonuç:", y)

    elif (islem == "9"):
        karekok = int(input("KareKök Bulunması İstenilen Sayıyı Giriniz:"))
        z = math.sqrt(karekok)
        print("Sonuç:", z)

    elif (islem == "10"):
        mutlak = int(input("Mutlak Değer Bulunması İstenilen Sayıyı Giriniz:"))
        c = math.fabs(mutlak)
        print("Sonuç:", c)

    else:
        print("Geçersiz İşlem")