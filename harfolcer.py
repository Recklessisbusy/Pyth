kelime = str(input("Kelime Girin:"))
sayac=0
for x in kelime:
    if x == "a" or x == "e" or x == "o" or x == "u" or x == "i":
       sayac += 1
print("Sesli Harf Sayısı: ",sayac)