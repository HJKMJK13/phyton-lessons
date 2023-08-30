# 1.
def salom_ber():
    """Salom beruvchi funksiya"""
    print("Assalomu aleykum")
salom_ber()

# 2.
def salom_ber(ism):
    """Foydalanuvchining ismini qabul qilib unga salom beruvchi funksiya"""
    print(f"Assalomu aleykum hurmatli {ism.title()}")
salom_ber('Karimjon')

# 3.docstring
def salom_ber(ism):
    """Foydalanuvchining ismini qabul qilib unga salom beruvchi funksiya"""
    print(f"Assalomu aleykum hurmatli {ism.title()}")
salom_ber('Karimjon')
print(salom_ber.__doc__) #--> docstringni konsolga chiqarish


# 4.Funksiyaga bir nechta argument kiritishga doir misol:

def salom_ber(ism,familya):
    """Foydalanuvchining ism familyasini chiqaruvchi funksiya"""
    print(f"Foydalanuvchining ismi:{ism.title()} \nFoydalanuvchining familyasi:{familya.title()}")
salom_ber('Karimjon','Norboyev')


#5. foydalanuchi va uning yoshini hisoblaydigan dastur:
def foydalanuvchi(ism,tugilgan_yili):
    """Foydalanuchi va uning yoshini hisoblaydigan dastur"""
    print(f"Foydalanuvchining ismi:{ism.title()} \nFoydalanuvchining yoshi:{2023-tugilgan_yili}")
foydalanuvchi('Karimjon', 2004)

# AMALIYOT

# =============================================================================
# #1.
# def foydalanuvchi(name,surname,yosh=20):
#     """Foydalanuvchi ism,familyasini yoshini chiqaruvchi dastur"""
# ism=input("Foydalanuvchi ismini kiriting:")
# familya=input("Foydalanuvchi familyasini kiriting:")
# print(f"Foydalanuvchining ismi:{ism.title()} \nFoydalanuvchining familyasi:{familya.title()} \nFoydalanuvchining yoshi:{yosh}")
# foydalanuvchi(ism,familya)
# 
# =============================================================================
#2.
def kiritilgan_son(num):
    
    print(f"{num} ni kvadrati:{num**2} \n{num} kubi:{num**3}")
kiritilgan_son(25)

#3.
def son_kirit(a):
   
    if a%2==0:
        print(f"{a} soni juft")
    else:
        print(f"{a} soni toq")
son_kirit(12)

#4.2 tasondan kattasini chiqarish:
def sonlar(son_1,son_2):
    if son_1>son_2:
        print(f"{son_1} katta {son_2}dan")
    elif son_1==son_2:
        print(f"{son_1} bn {son_2} teng")
    else:
        print(f"{son_2} katta {son_1}dan")
sonlar(24, 34)

#5.darajani hisoblash:
def numbers(x,y):
    print(f"{x} ning {y} darajasi {x**y} ga teng")
numbers(4, 3)
    
