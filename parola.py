import random
elemanlar = "+-/*!&$?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
uzunluk = int(input("Şifrenizin uzunluğunu girin: "))
x = ""
for i in range(uzunluk):
    x += random.choice(elemanlar)
print(x)
