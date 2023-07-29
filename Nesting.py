car_1={
       'model':'malibu',
       'narx':22000,
       'max_tezlik':215
       }

car_2={
       'model':'lacetti',
       'narx':16000,
       'max_tezlik':205
       }

car_3={
       'model':'matiz',
       'narx':6000,
       'max_tezlik':120
       }
cars=[car_1,car_2,car_3]
for car in cars:
    print(f"{car['model'].title()}, narxi:{car['narx']}$ , Maksimal tezligi:{car['max_tezlik']}")

#
print(cars[0]['model'],cars[0]['narx'],cars[0]['max_tezlik'])
print(cars[1]['model'],cars[1]['narx'],cars[1]['max_tezlik'])
print(cars[2]['model'],cars[2]['narx'],cars[2]['max_tezlik'])

#

lacettis=[]
for n in range(5):
    new_car={
        'model':'lacetti',
        'rang':None,
        'probeg':0,
        'Narx':None,
        'tezlik':200
        }
    lacettis.append(new_car)
# =============================================================================
# for lacetti in lacettis:
#     print(lacetti)
# =============================================================================
for lacetti in lacettis[:3]:
    lacetti['rang']='qora'
    
for lacetti in lacettis[3:5]:
    lacetti['rang']='kok'

for lacetti in lacettis:
    if lacetti['rang']=='qora':
       lacetti['Narx']=22000
    else:
        lacetti['Narx']=22500
    
for lacetti in lacettis:
    print(lacetti)
    
#Misol
kasblar={
    'Burjoq':['c#','phyton'],
    'Alisher':['java','c#'],
    'Islom':['html','css']
    }
for ism,kasblar in kasblar.items():
    print(f"{ism} quyidagi dasturlash tillarni biladi:")
    for til in kasblar:
        print(f"{til}")

#Amaliyot
#1.
shaxs_1={
    'ism':'ibn Ismoil',
    't_yili':810,
    't_joyi':'Buxoro'
    }
shaxs_2={
    'ism':'Abdulla Qodiriy',
    't_yili':1894,
    't_joyi':'Toshkent'
    }
shaxs_3={
    'ism':'Erkin Vohidov',
    't_yili':1936,
    't_joyi':'Farg\'ona'
    }
shaxs_4={
    'ism':'Alisher Navoiy',
    't_yili':1441,
    't_joyi':'Hirot'
    }
shaxslar=[shaxs_1,shaxs_2,shaxs_3,shaxs_4]
for shaxs in shaxslar:
    print(f"{shaxs['ism']} {shaxs['t_yili']}-yilda {shaxs['t_joyi']}da tug'ilgan")

#2.
shaxs_1={
    'ism':'ibn Ismoil',
    'asarlari':['Al-jome as-sahih','Al-adab al-mufrad','At-tari al-kabir']
    }
shaxs_2={
    'ism':'Abdulla Qodiriy',
    'asarlari':['O\'tkan kunlar','Mehrobdan chayon','Obid ketmon']
    }
shaxs_3={
    'ism':'Erkin Vohidov',
    'asarlari':['Tong nafasi','Qoshiqlarim sizga','O\'zbegim']
    }
shaxs_4={
    'ism':'Alisher Navoiy',
    'asarlari':['Xamsa','Lison ut-Tayr','Mahbub ul-Qulub']
    }
shaxslar=[shaxs_1,shaxs_2,shaxs_3,shaxs_4]
for shaxs in shaxslar:
    asarlar=shaxs['asarlari']
    print(f"{shaxs['ism']}ning mashxur asarlari:")
    for asar in asarlar:
        print(f"{asar}")

#3.

shaxs_1={
    'ism':'Islom',
    'kinolar':['Terminator','Rembo','Titanic']
    }
shaxs_2={
    'ism':'Burjoq',
    'kinolar':['Tenet','Inception','Interstaller']
    }
shaxs_3={
    'ism':'Mirzabek',
    'kinolar':['Abdullajon','Bomba','Shaytanat']
    }
shaxs_4={
    'ism':'Noilbek',
    'kinolar':['Qasoskorlar','Forsaj','Tezlik zavqi']
    }
shaxslar=[shaxs_1,shaxs_2,shaxs_3,shaxs_4]
for shaxs in shaxslar:
    kino=shaxs['kinolar']
    print(f"{shaxs['ism']}ning yoqtirgan  kinolari:")
    for kinolari in kino:
        print(f"{kinolari}")

#4.
davlat_1={
    'd_nomi':'O\'zbekiston',
    'poytaxti':'Toshkent',
    'hududi':448900,
    'aholisi':37.6
    }
davlat_2={
    'd_nomi':'Rossia',
   'poytaxti':'Moskva',
   'hududi':17098246,
   'aholisi':144
    }
davlat_3={
    'd_nomi':'AQSH',
   'poytaxti':'Vashington',
   'hududi':9631418,
   'aholisi':250
    }
davlatlar=[davlat_1,davlat_2,davlat_3]
for davlat in davlatlar:
    print(f"{davlat['d_nomi']} poytaxti:{davlat['poytaxti']} shaxri,\n Hududi:{davlat['hududi']} kv km,\n Aholisi:{davlat['aholisi']} mln")

