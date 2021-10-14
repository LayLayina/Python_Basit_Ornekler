print("""******************************
Faktöriyel Bulma Uygulaması
Kasım Can Arslan

Çıkmak İçin q ' ya Basınız.
""")


while True:
    sayı = input("Lütfen Faktöriyel Bulmak İstediğiniz Sayıyı Giriniz:")

    if (sayı == "q"):
        print("Program Sonlandırılıyor...")
        break


    sayı = int(sayı)

    faktoriyel = 1

    for i in range (2,sayı+1):
        faktoriyel *= i

    print("Faktöriyel:",faktoriyel)