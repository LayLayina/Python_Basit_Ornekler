print("""*****************************
Kullanıcı Giriş Uygulaması 2
Kasım Can Arslan
*****************************""")

sys_kullanıcı_adı = "kasımcan"
sys_kullanıcı_sifre = "237512"

kullanıcı_adı = input("Lütfen Kullanıcı Adınızı Giriniz:")
sifre = input("Lütfen Şifrenizi Giriniz:")

if (sys_kullanıcı_adı == kullanıcı_adı and sys_kullanıcı_sifre != sifre) :
    print("Şifre Yanlış")

elif (sys_kullanıcı_adı != kullanıcı_adı and sys_kullanıcı_sifre == sifre):
    print("Kullanıcı Adı Yanlış")

elif (sys_kullanıcı_adı != kullanıcı_adı and sys_kullanıcı_sifre != sifre):
    print("Kullanıcı Adı Ve Şifre Yanlış")

else:
    print("Giriş Başarılı Yönlendiriliyorsunuz...")