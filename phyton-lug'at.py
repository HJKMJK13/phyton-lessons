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

#Amaliyot

#1.
otam={"ismi":'Nizomjon',"yoshi":49}
print(f"Otamning ismi {otam['ismi']} yoshi {otam['yoshi']} da")
#print(f"onam {onam['ismi]} yoshi{onam['yoshi']}da")
