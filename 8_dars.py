mehmonlar=['Burjoq','Islom','Noil','Mirzabek']
for mehmon in mehmonlar:
    print("Salom",mehmon)
    print("Xayr",mehmon)
#2.
mehmonlar=['Burjoq','Islom','Noil','Mirzabek']
for mehmon in mehmonlar:
    print(f"hurmatli {mehmon} sizni toyga taklif qilamiz hurmat bilan palonchayevlar oilasi")
    


#3.son kvadratlarini chiqarib beradi.
sonlar=list(range(12))    
sonlar_kvadrati=[]
for son in sonlar:
    sonlar_kvadrati.append(son**2)
    print(sonlar_kvadrati)
    
    
#5.
dostlar=[]
#print("5 ta yaqin do'stinggizni ismini kiriting:")
#for n in range(5):
    #dostlar.append(input(f"{n+1}-dostingizni ismini kiriting:"))
#print(dostlar)


#6.
sonlar=list(range(5,50))
sonlar_kubi=[]
for sonlar in sonlar:
    sonlar_kubi.append((2*sonlar+1)**3)
print(sonlar_kubi)

#7.
sonlar=list(range(10,100))
for son in sonlar:
    if int(son+sonlar):
        print(int(son+sonlar))
    