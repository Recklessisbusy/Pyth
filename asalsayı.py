n = int(input("Sayı giriniz: "))
for sayi in range(2,n+1):
       for x in range(2,sayi):
           if (sayi % x) == 0:
               break
       else:
           print(sayi)