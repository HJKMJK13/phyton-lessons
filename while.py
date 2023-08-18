#1.
son=0
while son<=100:
    son=son+1
    print(son)
print("sikl to'xtadi")

#2.input va while
savol="Istalgan sonni kiriting"
savol +="(dasturni to'xtatish un 'exit' deb yozing):"
qiymat=''
while qiymat !='exit':
    qiymat=input(savol)
    if qiymat !='exit':
       print(float(qiymat)**2)
print("Dastur tugadi!")

#3.
sonlar=list(range(1,11))
for son in sonlar:
    if son==5:
        break
    print(f"{son}ning kvadrati {son**2} ga teng")

#4.continue--> tashlab ketish vazifasini bajaradi
sonlar=list(range(1,10))
for son in sonlar:
    if son==5:
        continue
    print(f"{son} ning kvadrati {son**2} ga teng")

#5.
son=0
while son<10:
    son+=1
    if son%2==0:
        continue
    else:
        print(son)
#6.
sonlar=list(range(1,100))
for son in sonlar:
    if son%2==0:
        continue
    print(son)   #--> toq sonlar chiqadi

#7.
sonlar=list(range(1,100))
for son in sonlar:
    if son%2==0:
       print(son)    #--> juft sonlar chiqadi