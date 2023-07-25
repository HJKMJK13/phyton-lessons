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

for lacetti in lacettis[:5]:
    lacetti['Narx']=22000
    
for lacetti in lacettis:
    print(lacetti)
