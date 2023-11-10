input = str(input("Kelime giriniz: "))
harf = "aeouiıüö"

def seslikontrol(kelime):
    sayac = 0
    for karakter in kelime.lower():
        if karakter in harf:
            sayac+= 1
    return sayac     
deger = seslikontrol(input)
print("Sesli harf sayısı:",deger)

#assert seslikontrol("GARDAŞ") == 2, 'Hatalı'
