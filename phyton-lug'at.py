#1.bu yerda kalit so'z va qiymat ishtirok qiladi model,rang--> kalit so'z ferrari, ko'k --> qiymat

car_0={"model":"Ferrari","rang":"ko'k"}
print(car_0["model"])
print(car_0["rang"])

#2.

eng_uz={"apple":"olma","banana":"banan","watermelon":"tarvuz"}
print(eng_uz["apple"])
print(eng_uz['banana'])
print(eng_uz['watermelon'])

#3.
talaba={"ism":"Karimjon","yosh":20,"yil":2003}
#print(f"Talabani ismi {talaba['ism']} yoshi {talaba['yosh']} da {talaba['yil']}da tug'ilgan")
#yangi kalit va qiymat qo'shish -->
talaba["kurs"]=3
talaba["fakultet"]="Amaliy matematika"
print(talaba)

#kalitni qiymatini o'zgartirish -->
talaba["ism"]='Mirzabek'
print(talaba)

#elementni o'chirish-->del elementlarni o'chirish vazifasini bajaradi
del talaba['fakultet']
print(talaba)

#get funksiyasi lug'atga kiritilgan kalit so'zlarni  ko'rib chiqadi  agar bo'lsa qiymatini qaytaradi bo'lmasa funksiyadagi javob qaytaradi 

#Amaliyot

# =============================================================================
# #1.
# otam={"ismi":'Nizomjon',"yoshi":49}
# print(f"Otamning ismi {otam['ismi']} yoshi {otam['yoshi']} da")
# =============================================================================
#print(f"onam {onam['ismi]} yoshi{onam['yoshi']}da")

# =============================================================================
# #2.
# oila={"ota":"osh","ona":"somsa","opam":"shashlik","ozim":"manti"}
# print(f"Oilamizda otam {oila['ota']}ni yaxshi ko'radi \
# onam {oila['ona']}ni yaxshi ko'radi \
# opam {oila['opam']}ni yaxshi koradi \
# ozim {oila['ozim']}ni yaxshi ko'raman")
# =============================================================================

# =============================================================================
# #3.
# lugat={"integer":"butun son","float":"o'nlik son","and":"va","or":"yoki"}
# soz=input("so'zni kiriting:")
# print(lugat.get(soz,'bunday soz mavjud emas'))
# =============================================================================

# =============================================================================
# mashina={"tezlik":"bugatti","chiroy":"royce","chidamlilik":"brabus"}
# tanlang=input("mashinani kirting:")
# print(mashina.get(tanlang,"bilmayman"))
# 
# =============================================================================
#Men haqimda
# =============================================================================
# men={"Ismim":"Karimjon","yoshim":20,"ovqat":"manti","rang":"yashil,ko'k"}
# soroq=input("Bilmoqchi bolgan malutmotingizni kiriting:")
# print(men.get(soroq,"Bu haqida malumot kiritilmagan"))
# =============================================================================

#4.
# =============================================================================
lugat={"integer":"butun son","float":"o'nlik son","and":"va","or":"yoki"}
soz=input('Kalit sozini kiriting:')
tarjima=lugat.get(soz)
if tarjima==None:
     print("Bunday so'z mavjud emas")
else:
     print(f"{soz} so'zi {tarjima} deb tarjima qilinadi")
# =============================================================================
    
###############################################################################
#2-qism -->Lug'atlar bilan ishlash

#1.items metodi
# =============================================================================
talaba={
         'yosh':'Karimjon',
         'familya':'Norboyev',
         'kurs':3,
         'yonalish':"Amaliy matematika"
         }
 #print(talaba.items())
for kalit,qiymat in talaba.items():
     print(f"Kalit:{kalit}")
     print(f"Qiymat:{qiymat} \n")
# =============================================================================
telefonlar={
    "Burjoq":"RED MI 10S",
    "Quvonchbek":'RED MI 11',
    "Karimjon":"OPPO RENO 7A",
    "Shoxruzbek":"Iphone 7"
    }
for kalit,qiymat in telefonlar.items():
    print(f"{kalit}ni telefoni: {qiymat}")

#2.keys metodi
mahsulotlar={
    'olma':20000,
    'uzum':24000,
    'banan':30000,
    'nok':32000,
    'shaftoli':25000
    }
#print(mahsulotlar.keys())
print("Dokondagi mahsulotlar:")
#1-usul
for mahsulot in mahsulotlar.keys():
    print(mahsulot.title())  
#2-usul 
for mahsulot in mahsulotlar:
    print(mahsulot.title())
# ikkala usuldan ham foydalansa boladi

#3.
bozorlik={'olma','uzum','non','baliq'}
for mahsulot in mahsulotlar:
    if mahsulot in bozorlik:
        print(f"{mahsulot}ning narxi {mahsulotlar[mahsulot]}")
for buyum in  bozorlik:
    if buyum not in mahsulotlar:
        print(f"Iltimos dokoninggizga {buyum} ham olib keling")

#4.
mashinalar={
    'malibu':20000,
    'nexia 3':10000,
    'gentra':15000,
    'matiz':6000,
    'lacetti':17000
    }
kerak={'bmw','gentra','mers','lacetti'}
for olaman in mashinalar:
    if olaman in kerak:
        print(f"{olaman}ning narxi {mashinalar[olaman]}")
for yoq in kerak:
    if yoq not in mashinalar:
        print(f"Iltimos {yoq}ni ham olib keling")

#5.
telefonlar={
    'samsung A21s':1800000,
    'redmi 10s':2800000,
    'oppo':2500000,
    'iphone 11':4600000,
    'iphone 14':10000000
    }
telefon_f={'redmi 11','iphone 14','oppo','realme'}
for olamiz in telefonlar:
    if olamiz in telefon_f:
        print(f"{olamiz}ni narxi:{telefonlar[olamiz]}")
for yoq_e in telefon_f:
    if yoq_e not in telefonlar:
        print(f"Iltimos {yoq_e}ni ham olib keling!")
        
# sorted funksiyasi --> Alifbo tartibida joylashtirib beradi
#1.
telefonlar={
    'samsung A21s':1800000,
    'redmi 10s':2800000,
    'oppo':2500000,
    'iphone 11':4600000,
    'iphone 14':10000000
    }
for telefon in sorted(telefonlar):
    print(telefon.title())
#2.
mashinalar={
    'malibu':20000,
    'nexia 3':10000,
    'gentra':15000,
    'matiz':6000,
    'lacetti':17000
    }
for mashina in sorted(mashinalar):
    print(mashina.title())
