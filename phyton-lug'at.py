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

#values metodi faqat qiymatlarni chiqarib beradi
#1.
mashinalar={
    'malibu':20000,
    'nexia 3':10000,
    'gentra':15000,
    'matiz':6000,
    'lacetti':17000
    }
for mashina in mashinalar.values():
    print(f"{mashina} $")
#2.
telefonlar={
    'samsung A21s':1800000,
    'redmi 10s':2800000,
    'oppo':2500000,
    'iphone 11':4600000,
    'iphone 14':10000000
    }
for telefon in telefonlar.values():
    print(f"{telefon} ming")

# set funksiyasi bir necha marotaba qatnashgan qiymatlarni bitta qilib ko'rsatadi
telefonlar={
    'Islom':"redmi note 8",
    'Burjoq ':"Redmi 10",
    'Mirzabek':"Redmi 10",
    'Dilshod ':"Iphone 12",
    'Quvonchbek':"Redmi 11",
    'Shoxruzbek':"Iphone 7",
    'Behruz':"Redmi 10"
    }
for telefon in set(telefonlar.values()):
    print(telefon)
    
# set aslida malumot turi unda takrorlangan elementlarni bitta qilib chiqarib beradi
oyinchoqlar={'bear','ball','car','bear','lamp'}
print(f"malumot turi -->{type(oyinchoqlar)}")
print(oyinchoqlar) # bir nechta elementlarni bitta qilib chiqarib beradi

#Amaliyot
#1.
lugat={
       'for':"takrorlanish sikli",
       'if':"shart operatori",
       'int':'butun sonlar',
       'float':"o'nlik sonlar",
       'and':'mantiqiy va operatori',
       'or':'mantiqiy yoki operatori' 
       }
for lugatlar in sorted(lugat):
    print(f"{lugatlar}-{lugat[lugatlar]}")

#2.
davlatlar={
    "O'zbekiston":'Toshkent',
    'Qozogiston':'Astana',
    'Turkmaniston':'Anqara',
    'Tojikiston':'Dushanbe',
    'Fransiya':'Parij',
    'Italiya':'Rim',
    'Ispaniya':'Madrid'
    }
print("Davlatlar ro'yxati:")
for davlat in sorted(davlatlar.keys()):
    print(davlat)
print("Poytaxtlar ro'yxati:")
for poytaxt in sorted(davlatlar.values()):
    print(poytaxt)
    
#3.
davlatlar={
    "O'zbekiston":'Toshkent',
    'Qozogiston':'Astana',
    'Turkmaniston':'Anqara',
    'Tojikiston':'Dushanbe',
    'Fransiya':'Parij',
    'Italiya':'Rim',
    'Ispaniya':'Madrid'
    }
davlat=input("Qaysi davlatni poytaxtini bilishni xohlysiz:").title()
poy=davlatlar.get(davlat)
if poy==None:
    print(f"kechirasiz {davlat} haqida malumot yoq")
else:
    print(f"{davlat}ni poytaxti {poy} shahri")

#4.
menu={
      'manti':12000,
      'osh':18000,
      'somsa':8000,
      'shashlik':13000,
      'norin':20000,
      'shorva':10000,
      'non':3000,
      'choy':2000
      }
print("3 ta taom buyurtma bering:")
buyurtmalar=[]
for n in range(3):
    buyurtmalar.append(input(f"{n+1}-taom:"))
for buyurtma in buyurtmalar:
    if buyurtma in menu:
        print(f"{buyurtma}ni narxi {menu[buyurtma]}so'm")
    else:
        print(f"kechirasiz  {buyurtma} yoq edi")

#qo'shimcha:
yonalishlar={
    'TM-2101':20,
    'TM-2102':19,
    'TM-2103':18,
    'ATT':54,
    'KIDT':46,
    'AX':23
    }
print("3 ta yonalishni tanlang")
talabalar=[]
for n in range(3):
    talabalar.append(input(f"{n+1}-yonalish:").upper())
for talaba in talabalar:
    if talaba in yonalishlar:
        print(f"{talaba}da:{yonalishlar[talaba]} o'qiydi.")
    else:
        print("Bu yonalish haqida malumot berilmagan!")
    
    

