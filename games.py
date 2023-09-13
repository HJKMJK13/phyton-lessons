import random
def sontop(x=10):
    tasodifiy_son=random.randint(1, x)
    print("Men bir son o'yladim topa olasizmi ?")
    taxminlar=0
    while True:
        taxmin=int(input("-->"))
        taxminlar +=1
        if taxmin<tasodifiy_son:
            print("Xato.Men o'ylagan son kiritgan soninggizdan kattaroq")
        elif taxmin>tasodifiy_son:
            print("Xato.Men o'ylagan son kiritgan soninggizdan kichikroq")
        else:
            break
    print(f"Tabriklaymiz.{taxminlar} ta taxmin bilan topdingiz")
