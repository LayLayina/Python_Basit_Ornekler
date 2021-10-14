

print("""*******************************
0'dan 10'e Kadar Olan Çift Sayıların Toplamını Yazdıran Uygulama
Kasım Can Arslan
*******************************""")

sayac = 0
toplam = 0
while sayac <= 10:
    sayac = sayac + 2
    toplam = toplam + sayac

print("0 ile 10 arasındaki çift sayıların toplam:{0}".format(toplam))
