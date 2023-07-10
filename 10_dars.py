# =============================================================================
# 
#2.
# =============================================================================
# 

# =============================================================================
# #3.
# ovqat=['osh','manti','lagmon','somsa','shashlik']
# buyurtma=input('nima zakaz qilasiz?')
# if buyurtma in ovqat:
#     print('tezda tayyor boladi')
# else:
#     print("bizda unaqa ovqat qolmagandi!")
# =============================================================================

# =============================================================================
# menu = ['osh','qazonkabob','shashlik','norin','somsa']
# buyurtmalar = ["osh","somsa","manti", "shashlik"]
# 
# for taom in buyurtmalar:
#     if taom in menu:
#         print(f"Menuda {taom} bor")
#     else:
#         print(f"Kechirasiz, menuda {taom} yo'q")
#     
# =============================================================================
# =============================================================================
# #4.
# menu=['osh','somsa','shashlik','lagmon','shorva','manti']
# buyurtmalar=['osh','somsa','choy']
# for taom in buyurtmalar:
#     if taom in menu:
#         print(f"menuda {taom} bor")
#     else:
#         print(f"menuda {taom} yoq")
# =============================================================================
#5.
# =============================================================================
# son=int(input("Juft sonni kiriting!"))
# if son%2==0:
#     print("Raxmat")
# else:
#     print("Bu juft son emas!")
# =============================================================================
#6.
# =============================================================================
# yosh=int(input("yoshingizni kiriting:"))
# if yosh<4:
#     print("sizgi kirish bepul!")
# elif yosh>4 and yosh<18:
#     print("sizga kirish 10000 so'm")
# elif yosh>18 and yosh<60:
#     print("Sizga kirish 20000 so'm")
# elif yosh>60:
#     print("sizga kirish bepul!")
# =============================================================================

#7.
son_1=int(input('1-sonni kiriting:'))
son_2=int(input('2-sonni kiriting:'))
if son_1>son_2:
    print(f"{son_1}>{son_2}")
elif son_1<son_2:
    print(f"{son_1}<{son_2}")
else:
    print(f"{son_1}={son_2}")