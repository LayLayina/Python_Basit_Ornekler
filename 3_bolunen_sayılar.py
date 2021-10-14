#1'den 100'e kadar olan sayılardan sadece 3'e bölünen sayıları ekrana bastırın. Bu işlemi continue ile yapmaya çalışın.

print("""***************************************
1'den 100'e Kadar 3'e Tam Bölünen Sayılar
Kasım Can Arslan
***************************************
""")

for i in range(1,101):
    if (i % 3 != 0):
        continue
    print(i)
