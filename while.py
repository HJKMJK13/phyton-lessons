#1.
# =============================================================================
# son=0
# while son<=100:
#     son=son+1
#     print(son)
# print("sikl to'xtadi")
# =============================================================================

# =============================================================================
# #2.input va while
# savol="Istalgan sonni kiriting"
# savol +="(dasturni to'xtatish un 'exit' deb yozing):"
# qiymat=''
# while qiymat !='exit':
#     qiymat=input(savol)
#     if qiymat !='exit':
#         print(float(qiymat)**2)
# print("Dastur tugadi!")
# =============================================================================

#3.Ishora orqali siklni to'xtatish
# =============================================================================
# savol=input("Istalgan sonni kiriting(dasturni to\'xtatish un 'exit' deb yozing):")
# ishora=True
# while ishora:
#       qiymat=input(savol)
#       if qiymat=='exit':
#          ishora=False
#       else:
#          print(float(qiymat)**2)
# =============================================================================
      
#4.break operatori
# =============================================================================
# savol=input("Istalgan sonni kiriting(dasturni to\'xtatish un 'exit' deb yozing):")
# while True:
#     qiymat=input(savol)
#     if qiymat=='exit':
#         break
#     else:
#         print(float(qiymat)**2)
# =============================================================================

#5.
sonlar=list(range(1,11))
for son in sonlar:
    if son==5:
        break
    print(f"{son} ning kvadrati {son**2} ga teng")