print("""******************************
Beden Kitle Endeks Hesaplama Programı
Kasım Can Arslan
******************************""")

kilo = int(input("Lütfen Kilonuzu Giriniz:"))
boy = float(input("Lütfen Boyunuzu Giriniz: "))

bki = kilo / (boy ** 2)

if (bki <= 18.5):
    print("Zayıfsınız")

elif (bki >= 18.5 and bki <= 25):
    print("Normalsiniz")

elif (bki >= 25 and bki <= 30):
    print("Fazla Kilolusunuz")

elif (bki >= 30):
    print("Obezsiniz")

