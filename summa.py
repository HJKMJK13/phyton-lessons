#1.
def summa(*sonlar):
    yigindi=0
    for son in sonlar:
        yigindi+=son
    return yigindi
print(summa(44,45,46,47,48))

#2.juft sonlar yigindisi hisoblovchi dastur
def yigin(*numbers):
    mus=0
    for num in numbers:
        if num%2==0:
            mus+=num
    return mus
print(yigin(23,24,25,26,27,28))
#3.
def yigindi_3(*sonlar):
    return sum(sonlar)
print(yigindi_3(34,35,36,37))

#4. kwargs
def avto_info(kompaniya,model,**malumotlar):
    malumotlar['kompaniya']=kompaniya
    malumotlar['model']=model
    return malumotlar
avto_1=avto_info('GM', 'malibu', yil=2020,narxi=35000)
avto_2=avto_info('Kia', 'k5', yil=2022,narxi=34000,rang='qora')
print(avto_1,avto_2)\
#5.berilgan sonlar kopaytmasini chiqaruvchi dastur
def kopaytma(*numbers):
    kopayt=1
    for  num in numbers:
        kopayt *=num
    return kopayt
print(kopaytma(1,2,3,4))

#6.Berilgan sondan berilgan songacha bolgan sonlar yigindisi aytaylik(1 dan 100 gacha) -->
def son(n):
    number=0
    for numbers in range(1,n):
        number += numbers
    return number
print(son(100))

#7. berilgan sondan berilgan songacha bolgan sonlar kopaytmasini chiqaruvchi dastur(aytaylik 1 dan 100 gacha)-->
def kopaytma(n):
    kopay=1
    for num in range(1,n):
        kopay *=num
    return kopay
print(kopaytma(100))

#8. kwargs yordamida talaba haqida malumot kiritamiz
def talaba_m(ism,familya,**news):
    news['Ism']=ism
    news['Familya']=familya
    return news
new_1=talaba_m('Karimjon', 'Norboyev', yoshi=20,tugilgan_joyi='Buxoro')
print(new_1)

#9.Davlatlar haqida malumot
def country(nom,poytaxt,**new):
    new['Nomi']=nom
    new['Poytaxti']=poytaxt
    return new
country_1=country("O'zbekiston", 'Toshkent', aholi=38000000,maydoni=448900,viloyati=13)
country_2=country('Qozogiston', 'Astana', aholi=20000000,maydoni=2800000,viloyat=17)
print(country_1)
print(country_2)


