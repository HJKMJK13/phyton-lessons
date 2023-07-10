mevalar=["olma","anor","banan","shaftoli"]
mevalar[0]='uzum'
print(mevalar)

#1.append --> har doim royxatni oxiriga qiymat qo'shadi
mevalar=["olma","anor","banan","shaftoli"]
mevalar.append('uzum')
print(mevalar)

#2.insert --> royxatni istalgan joyiga  qiymatni qoshadi avval indeksi yoziladi keyin qiymati yoziladi
mevalar=["olma","anor","banan","shaftoli"]
mevalar.insert(3,"o'rik")
print(mevalar)
# bu yerda 3 indeksi o'rik qiymati

#3. remove ro'yxatdagi elementni o'chirish uchun qo'llanadi
cars=["bmw",'mers','gentra','nexia','malibu','matiz']
cars.remove("malibu")
print(cars)
#remove element birt necha marotaba qatnashgan bolsa faqat birinchisini topib oshani ochiradi hammasdini
#oshirish uchun removdan bir necha marotaba foydalanish kk 
cars=["bmw",'mers','gentra','nexia','malibu','matiz',"malibu"]
cars.remove("malibu")
cars.remove("malibu")
print(cars)

#4.pop korsatilgan indeksdagi elementni ajratib oladi
royxat=['un','yog','piyoz','gosht']
olindi=royxat.pop(3)
print('olingan mahsulotlar:',olindi)
print('qolgan mahsulotlar:',royxat)
# agar hech qanday indeks korsatilmasa royxat oxiridagi elementni ajratrib oladi

#Amaliyot

#1.
ismlar=['Islom','Noil','Dilshod']
print('Salom',ismlar[0])
print(ismlar[1],"bugun choyxonaga boramizmi?")

#2.
sonlar=[-23,6,45,-36,567,234]
c=sonlar[1]+sonlar[4]
print(c)
sonlar[0]=24
g=sonlar[0]+sonlar[1]
print(g)

#3.
t_shaxslar=['Navoiy','Beruniy','Ibn Sino']
z_shaxslar=['Bill Geyts','Jobs','Sukerberg','Mask']
print('Men tarixiy shaxslardan ',str(t_shaxslar[1]),' bilan zamonaviy shaxslardan ',str(z_shaxslar[1]),' bilan suhbat qilishni istardim')

#4.
friends=[]
friends.append("Burjoq")
friends.append("Dilshod")
friends.append("Islom")
print(friends)
#friends.remove(1)
print("Mehmonga keladiganlar:",friends)

#5.
friends=[]
friends.insert(0,'Quvonchbek')
friends.append("Burjoq")
friends.append("Dilshod")
friends.append("Islom")
friends.append('Shoxruzbek')
print(friends)
print(friends)
friends.remove('Dilshod')
print("Mehmonga keladiganlar:",friends)

#6.
friends=[]
friends.insert(0,'Quvonchbek')
friends.append("Burjoq")
friends.append("Dilshod")
friends.append("Islom")
friends.append('Shoxruzbek')
mehmonlar=[]
d_1=friends.pop(0)
d_2=friends.pop(1)
d_3=friends.pop(2)
mehmonlar.append(d_1)
mehmonlar.append(d_2)
mehmonlar.append(d_3)
print("mehmonlar:",mehmonlar)