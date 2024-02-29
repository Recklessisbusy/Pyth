girdi = str(input("Kelime Girin:"))
deneme = "aeuüoöıi"
def kontrol(kelime):
    sayac = 0
    for harf in kelime.lower:
        if harf in deneme:
            sayac+=1
    return sayac

t = kontrol(girdi)
print("Sesli Harf Sayısı:",t)