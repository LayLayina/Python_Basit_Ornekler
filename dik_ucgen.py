print("""------------------------------
Dik Üçgen Hipotenüs Hesaplama Programı
Kasım Can Arslan
------------------------------""")

print("Birbirine Dik Olan;")

kenar1 = int(input("Lütfen 1.Kenarın Uzunluğunu Giriniz:"))
kenar2 = int(input("Lütfen 2.Kenarın Uzunluğunu Giriniz:"))

kenar3 = (kenar1 ** 2 + kenar2 ** 2) ** 0.5


print("\nHipotenüs: {}".format(kenar3))

