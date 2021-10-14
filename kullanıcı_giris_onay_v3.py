print("""*********************************
Kullanıcı Giriş Programı
Kasım Can Arslan
*********************************""")

sys_kullanıcı = laylayina
sys_parola = 237512

giris_hakkı = 3

while True:
    kullanıcı_adı = input("Lütfen Kullanıcı Adınızı Giriniz:")
    parola = input("Lütfen Parolanızı Giriniz:")

    if (sys_kullanıcı != kullanıcı_adı and sys_parola == parola):
        print("Kullanıcı Adı Hatalı...")
        giris_hakkı -= 1
        print("Giriş Hakkı:",giris_hakkı)

    elif (sys_kullanıcı == kullanıcı_adı and sys_parola != parola):
        print("Şifre Hatalı....")
        giris_hakkı -= 1
        print("Giriş Hakkı:",giris_hakkı)

    elif (sys_kullanıcı != kullanıcı_adı and sys_parola != parola):
        print("Kullanıcı adı ve Şifre Hatalı...")
        giris_hakkı -= 1
        print("Giriş Hakkı:",giris_hakkı)

    else:
        print("Sisteme Başarıyla Giriş Yapıldı...")
        break

    if (giris_hakkı == 0):
        print("Giriş Hakkınız Doldu...")
        break