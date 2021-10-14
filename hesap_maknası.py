print("""*******************************
Hesap Makinası Programı
Kasım Can Arslan

İşlemler;

1. Toplama
2. Çıkarma
3. Bölme
4. Çarpma
*******************************""")


a = float(input("Lütfen İşlem Yapılacak 1.Sayıyı Giriniz:"))
b = float(input("Lütfen İşlem Yapılacak 2.Sayıyı Giriniz:"))

islem = input("Lütfen Yapmak İstediğiniz İşlemi Giriniz:")

if islem == "1" or "Toplama" or "toplama":
    print("İşlem Sonucu: {} ".format(a + b))

elif islem == "2" or "Çıkarma" or "çıkarma" or "cıkarma":
    print("İşlem Sonucu: {}".format(a - b))

elif islem == "3" or "Bölme" or "bolme" or "bölme":
    print("işlem Sonucu: {} ".format(a / b))

elif islem == "4" or "Çarpma" or "carpma" or "çarpma":
    print("İşlem Sonucu:{} ".format(a * b))

else :
    print("Geçersiz İşlem")