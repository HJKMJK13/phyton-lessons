#1.
import math
uzunlik=lambda pi,r:2*pi*r
print(uzunlik(math.pi,10))
#2.
def daraja(n):
    return lambda x:x**n
kvadrat=daraja(2)
kub=daraja(3)
#3.
from math import exp
sonlar=list(range(26))
ildizlar=list(map(exp, sonlar))
print(ildizlar)

#4.
from math import exp
numbers=list(range(101))
daraja=list(map(exp,numbers))
print(daraja)

#5.
sonlar=list(range(101))
def daraja2(x):
    return x*x
natija=list(map(daraja2,sonlar))
print(natija)

#6. berilgan sonlar kvadratini lambda funksiyasi orqali chiqarish
sonlar=list(range(101))
kvadrat=list(map(lambda x:x*x,sonlar))
print(kvadrat)

#7. filter yordamida  sonlar ichidan tasodifiy n tasini chiqaruvchi dastur
import random as r
sonlar=r.sample(range(100),10)
def juft_s(x):
    return x%2==0
juft=list(filter(juft_s,sonlar))
print(juft)

