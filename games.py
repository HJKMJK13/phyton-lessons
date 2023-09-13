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
    print(f"Tabriklayman.{taxminlar} ta taxmin bilan topdingiz")
    return taxminlar
def bizni_son(x=10):
    input(f"1 dan {x} gacha biror son o'ylang va biror tugmani bosing.Men topaman")
    quyi=1
    yuqori=x
    taxminlar=0
    while True:
        taxminlar +=1
        if quyi != yuqori:
            taxmin=random.randint(quyi, yuqori)
        else:
            taxmin=quyi
        javob=input(f"Siz {taxmin} sonini o'yladingiz:To'g'ri(t),"
                    f"Men o'ylagan son kattaroq(+),yoki kichikroq(-)".lower())
        if javob=="-":
            yuqori=taxmin-1
        elif javob=="+":
            quyi=taxmin+1
        else:
            break
    print(f"Men {taxminlar} ta taxmin bilan topdim")
    return taxminlar
def play(x=10):
    yana=True
    while yana:
        taxminlar_user=sontop(x)
        taxminlar_pc=bizni_son(x)
        if taxminlar_user>taxminlar_pc:
            print("Men yuttim")
        elif taxminlar_pc>taxminlar_user:
            print("Siz yutdingiz.Tabrikliman")
        else:
            print("Durrang!")
        yana=int(input("Yana o'ynaysizmi?Ha(1)/Yoq(0):"))
        
            
