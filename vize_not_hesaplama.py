print("""**********************************
Vize ve Final Not Hesaplama Programı
Kasım Can Arslan
**********************************""")

vize1 = float(input("Lütfen 1.Vize Puanınızı Giriniz:"))
vize2 = float(input("Lütfen 2.Vize Puanınızı Giriniz:"))
final = float(input("Lütfen Final Puanınızı Giriniz:"))

genelnot = vize1 * 3/10 + vize2 * 3/10 + final * 4/10

if (genelnot >= 90):
    print("AA")

elif (genelnot >= 85):
    print("BA")

elif (genelnot >= 80):
    print("BB")

elif (genelnot >= 75):
    print("CB")

elif (genelnot >= 70):
    print("CC")

elif (genelnot >= 65):
    print("DC")

elif (genelnot >= 60):
    print("DD")

elif (genelnot >= 55):
    print("FD")

else:
    print("FF")