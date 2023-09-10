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
