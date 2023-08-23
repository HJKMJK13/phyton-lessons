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
print(salom_ber.__doc__)
