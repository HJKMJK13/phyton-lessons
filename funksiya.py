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
    print(f"{x} ning {y}-darajasi {x**y} ga teng")
numbers(4, 3)

#6.Berilgan sonning qatiy darajasinin chiqaruvchi funksiya:
def number(x,y=2):
    print(f"{x} ning kvadrati {x**y} ga teng")
number(24)
#7.
def num(x):
    for n in range(2,11):
        if x%n==0:
            print(f"{x} {n} ga qoldiqsiz bolinadi")
num(24)

# birdan yuzgacha bolgan sonlar orasida 3 ga bolinadigani
def bolinish(x):
    for n in range(1,100):
        if n%x==0:
            print(f"{n}--> 3 ga bo'linadi")
bolinish(3)

#
def text(x):
    for n in range(1,100):
        print(f"{n}.{x}")
text("Man o'zimni yaxshi ko'raman  ❤️❤️")

#
def fibonacci(n):
    sonlar = []
    for x in range(n):
        if x == 0 or x == 1:
            sonlar.append(1)
        else:
            sonlar.append(sonlar[x - 1] + sonlar[x - 2])
    return sonlar


print(fibonacci(10))
#
def fibonachi_2(n):
    numbers=[]
    for x in range(n):
        if x==0 or x==1:
            numbers.append(1)
        else:
            numbers.append(numbers[x-1]+numbers[x-2])
        return numbers
fibo=fibonachi_2(100)

            

    
