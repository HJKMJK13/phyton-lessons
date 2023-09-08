def toliq_ism_yasa(ism,familya):
    """To'liq ism familya"""
    toliq_ism=f"{ism} {familya}"
    return toliq_ism
talaba=toliq_ism_yasa("Karimjon", "Norboyev")
print(talaba)
#2.
def names(ism,familya,otasining_ismi=''):
    if otasining_ismi:
        name=f"{ism} {familya} {otasining_ismi}"
    else: 
        name=f"{ism} {familya}"
    return name.title()
talaba=names('Karimjon', 'Norboyev',"Nizomjon o'gli")
print(talaba)

#3.
def avto_info(kompaniya,model,rangi,yili,narxi=None):
    avto={'kompaniya':kompaniya,
        'model':model,
        'rang':rangi,
        'yil':yili,
        'narx':narxi
        }
    return avto
car1=avto_info('GM','lacetti','oq',2018)
car2=avto_info('GM','nexia2','qora',2019,9000)
cars=[car1,car2]
print('Onlayn bozordagi mashinalar narxi:')
for avtolar in cars:
    if avtolar['narx']:
        narx=avtolar['narx']
    else:
        narx='Nomalum'
    print(f"{avtolar['rang']} {avtolar['model']}. Narxi:{narx}$")
        
#Amaliyot
#1.
def foydalanuvchi(ism,familya,t_y,t_j,email,t_r):
    shaxs={'ism':ism,
           'familya':familya,
           'tugilgan_yili':t_y,
           'tugilgan_joyi':t_j,
           'email':email,
           'tel_raqam':t_r
        }
    return shaxs
shaxs_1=foydalanuvchi('Karimjon', 'Norboyev', 2004, 'Buxoro','norboyevkarimjon06@gmail.com', 941208010)
print(shaxs_1)

#3.
def mijoz_info(ism, familiya, tyil, tjoy, email="", tel=None):
    """Mijoz haqidagi ma'lumotlarni lug'at ko'rinishida qaytaruvchi funksiya"""
    mijoz = {
        "ism": ism,
        "familiya": familiya,
        "tyil": tyil,
        "yoshi": 2020 - tyil,
        "tjoy": tjoy,
        "email": email,
        "telefon": tel,
    }
    return mijoz


print("Mijoz haqida ma'lumotlarni kiriting.")
mijozlar = []
while True:
    ism = input("Ismi: ")
    familiya = input("Familiyasi: ")
    tyil = int(input("Tug'ilgan yili: "))
    tjoy = input("Tug'ilgan joyi: ")
    email = input("Email: ")
    telefon = input("Telefon raqami: ")
    mijozlar.append(mijoz_info(ism, familiya, tyil, tjoy, email, telefon))
    javob = input("Davom etasizmi? (ha/yo'q)")
    if javob != "ha":
        break

print("Mijozlar:")
for mijoz in mijozlar:
    print(
        f"{mijoz['ism'].title()} {mijoz['familiya'].title()},"
        f"{mijoz['yoshi']} yoshda, telefoni: {mijoz['telefon']}"
    )
#4.
# =============================================================================
# sonlar=[]
# while True:
#     son_1=int(input("Birinchi sonni kiriting:"))
#     son_2=int(input("Ikkinchi sonni kiriting:"))
#     son_3=int(input("Uchinchi sonni kiriting:"))
#     sonlar.append(son_1,son_2,son_3)
#     for son in sonlar:
#         if son_1>son_2 and son_1>son_3:
#             print(f"{son_1} eng katta")
#         elif son_2>son_1 and son_2>son_3:
#             print(f"{son_2} eng katta")
#         else:
#             print(f"{son_3} eng katta")
#             break
#   
# 
# =============================================================================
# Sonlardan kattasini topuvchi funksiya
def kattasi(x, y, z):
    max = x
    if y >= max:
        max = y
    if z >= max:
        max = z
    return max
sonlar=kattasi(23, 25, 30)
print(f"{sonlar} eng kattasi")

#sonlardan eng kichikinasini chiqaruvchi dastur
def kichkinasi(a,b,c):
    min=a
    if b<=min:
        min=b
    if c<=min:
        min=c
    return min
numbers=kichkinasi(24, 35, 57)
print(f"{numbers} sonlarning eng kichigi")
# Aylana yuzi,uzunligi diametrini chiqarish dasturi
def radius(x,pi=3.14):
    s={
       'radius':x,
       'diametr':2*x,
       'yuz':pi*x*x,
       'aylana_u':2*pi*x
       }
    return s
yuz=radius(5)
print(yuz)

#To'g'ri to'rtburchak yuzi,perimetri-->
def t_t(a,b):
    togri={
        'perimetr':2*(a+b),
        'yuzi':a*b
        }
    return togri
tort=t_t(5,6)
print(tort)



