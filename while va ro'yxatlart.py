#1.Yaqin do'stlarimiz ro'yxatini tuzish
ismlar=[]
n=1
while True:
    savol=f"{n}-do'stingizni ismini kiriting:"
    name=input(savol)
    ismlar.append(name)
    n+=1
    takrorlash=input("Kiritishda davom qildirasizmi:")
    if takrorlash !='ha':
        break
print("Do'stlaringiz ro'yxati")
for ism in ismlar:
     print(ism.title())

#2.yoqtirgan mashinalarimiz ro'yxatini tuzamiz
print("O'zimizga yoqqan mashinalr ro'yxatini tuzamiz:")
mashinalar=[]
n=1
while True:
    savol=f"{n}-mashina:"
    car=input(savol)
    mashinalar.append(car)
    n+=1
    takrorlash=input('Yana kiritamizimi:')
    if takrorlash!='ha':
        break
print('Mashinalar ro\'yxati:')
for mashina in mashinalar:
    print(mashina.title())

#3.
dostlar={}
ishora=True
while ishora:
    ism=input('Do\'stingizni ismini kiriting:')
    yosh=input(f"{ism}ni yoshini kiriting:")
    dostlar[ism]=int(yosh)
    takrorlash=input('Davom qildirasizmi:')
    if takrorlash!="ha":
        ishora=False
print('Kiritilgan malumotlar:')
for malumot in dostlar.items():
    print(f"{ism.title()}ni yoshi {yosh} da")

#4.
cars=['matiz','nexia','damas','matiz','lacetti','cobalt','matiz']
car='matiz'
while car in cars:
     cars.remove(car)
print(cars)

#Amaliyot
#1.Foydalanuvchidan buyurtma qabul qiluvchi dastur!
buyurtmalar=[]
n=1
while True:
    savol=f"{n}-buyurtmani kiriting:"
    zakaz=input(savol)
    buyurtmalar.append(zakaz)
    n+=1
    takrorlash=input("Yana buyurtma berasizmi:")
    if takrorlash !='ha':
        break
print("Buyurtmalar ro'yxati:")
for buyurtma in buyurtmalar:
    print(buyurtma.title())

#2.Bozor uchun mahsulotlar va ularning narxini shakllantiruvchi dastur!
bozor={}
ishora=True
n=1
while ishora:
    mahsulot=input(f"{n}-mahsulotni kiriting:")
    narx=input(f"{mahsulot}nig narxini kiriting:")
    bozor[mahsulot]=int(narx)
    takrorlash=input('Davom qildirasizmi:')
    n+=1
    if takrorlash !='ha':
        ishora=False
print("Kiritildan mahsulotlar va ularni narxlari:")
for buyurtma in bozor.items():
    print(f"{mahsulot.title()}ni narxi {narx}")

#3.Bozordagi mashinalar va ularni narxlari:
bozor={}
ishora=True
n=1
while ishora:
    mashinalar=input(f"{n}-mashina nomini kiriting:")
    narx=input(f"{mashinalar}ning narxini kiriting:")
    bozor[mashinalar]=int(narx)
    takrorlash=input('Davom qildiramizmi:')
    n+=1
    if takrorlash !='ha':
        ishora=False
print('Kiritilgan mashina va ularning narxi:')
for mashina in bozor.items():
    print(f"{mashinalar.title()}ning narxi {narx} $")
