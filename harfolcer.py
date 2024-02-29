kelime = str(input("Kelime Girin:"))
sayac=0
for x in kelime:
    if x in "aeouüiöı" :
       sayac += 1
print("Sesli Harf Sayısı: ",sayac)