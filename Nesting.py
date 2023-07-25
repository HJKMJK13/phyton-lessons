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
    print(f"{car['model'].title()}, {car['narx']}$ , Maksimal tezligi:{car['max_tezlik']}")

