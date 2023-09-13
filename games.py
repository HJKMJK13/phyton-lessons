import random
def sontop(x=10):
    tasodifiy_son=random.randint(1, x)
    print("Men bir son kirittim topa olasizmi ?")
    
    while True:
        taxmin=int(input("-->"))
        if taxmin<tasodifiy_son:
            print("Xato.Men o'ylagan son kiritgan soninggizdan kattaroq")
        elif taxmin>tasodifiy_son:
            print("Xato.Men o'ylagan son kiritgan soninggizdan kichikroq")
        else:
            break
    print("Tabriklaymiz.Topdingiz")