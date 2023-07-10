# -*- coding: utf-8 -*-
"""
Created on Thu Jun 22 11:49:52 2023

@author: hp
"""
#1.
ism="Karimjon"
viloyat="Buxoro"
matn="Man yangi 📱 oldim"
smile="✈"
print(matn)

#2.
ism="Karimjon"
print("Mening ismim",ism)
print("Mening ismim "+ism)

#3.

ism="Karimjon"
familya="Norboyev"
print(ism + "  " + familya )

#4.fstring usuli
ism="Karimjon"
familya="Norboyev"
ism_familya=f"{ism} {familya}"
print(ism_familya)

#5.
ism="Karimjon"
familya="Norboyev"
print(f"mening ismim {ism} {familya}")

#6.Hammasini katta harf bilan yozish
ism="Karimjon"
familya="Norboyev"
ism_familya=f"{ism} {familya}"
ism_sharif=ism_familya.upper()
print(ism_sharif)

#7.birinchi harfni katta qilish
ism="karimjon"
familya="norboyev"
ism_familya=f"{ism} {familya}"
ism_sharif=ism_familya.title()
print(ism_sharif)

#8.birinchi so'zni birinchi harfi katta harf bo'lishi
ism="karimjon"
familya="norboyev"
ism_familya=f"{ism} {familya}"
ism_sharif2=ism_familya.capitalize()
print(ism_sharif2)

#9.so'zni boshidagi va oxiridagi bo'sh joylarni olib tashlaydi
matn="     meva     "
print("Man ko'chadan "+matn.lstrip()+ " oldim")
print("Man ko'chadan "+matn.strip()+" oldim")

#10.
ism=input("ismingizni kiriting:")
print("Assalomu aleykum "+ism.upper())

#Amaliyot

#1.
kocha="Bog'bon"
mahalla="Sog'bon"
tuman="Bodomzor"
viloyat="Samarqand"
print(kocha+" ko\'chasi," + mahalla+  " mahallasi," + tuman+" tumani,"+ viloyat+" viloyati")

#2.
kocha="Yuqori shayxlar"
mahalla="Shayxlar"
tuman="Olot"
viloyat="Buxoro"
print(kocha+" ko\'chasi," +mahalla+" mahallasi," + tuman+ " tumani," + viloyat+" viloyati" )

#3.
kocha="Yuqori shayxlar"
mahalla="Shayxlar"
tuman="Olot"
viloyat="Buxoro"
print(kocha+" ko\'chasi,\n"+mahalla+" mahallasi,\n"+ tuman+ " tumani,\n" + viloyat+" viloyati" )

#4.
kocha="Yuqori shayxlar"
mahalla="Shayxlar"
tuman="Olot"
viloyat="Buxoro"
print(f"{kocha} kochasi,{mahalla} mahallasi,{tuman} tumani,{viloyat} viloyati")