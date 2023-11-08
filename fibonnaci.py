n= int(input("Kaçıncı Değeri Bulunsun: "))
say = 0 
x = 0
y=1
a=3
print("1.Değer: ",x)
print("2.Değer: ",y)
while say < (n-2) :
    z=y+x
    print(str(a)+"."+"Değer: ", z)
    x=y
    y=z
    say += 1
    a+=1