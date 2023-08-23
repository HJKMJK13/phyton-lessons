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

# 4.
def salom_ber(ism,familya):
    """Foydalanuvchining ism familyasini chiqaruvchi funksiya"""
    print(f"Foydalanuvchining ismi:{ism.title()} \nFoydalanuvchining familyasi:{familya.title()}")
salom_ber('Karimjon','Norboyev')
