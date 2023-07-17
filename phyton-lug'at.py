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
lugat={"integer":"butun son","float":"o'nlik son","and":"va","or":"yoki"}
soz=input('Kalit sozini kiriting:')
tarjima=lugat.get(soz)
if tarjima==None:
    print("Bunday so'z mavjud emas")
else:
    print(f"{soz} so'zi {tarjima} deb tarjima qilinadi")
