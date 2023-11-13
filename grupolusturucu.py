import random
n = int(input("Kaçarlı gruplar kurucalacak?: "))
x = int(input("Kaç kişi olucak?: "))
liste = []
g=1
for i in range(0,x):
    liste.append(str(input("İsim giriniz: ")))
for z in range(0,int(x/n)):
    print(str(g)+".Grup:")
    for c in range(0,n):
        a = random.choice(liste)
        print(a)
        liste.remove(a)
    g += 1
