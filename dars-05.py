kocha="Bog'bon"
mahalla="Sog'bon"
tuman="Bodomzor"
viloyat="Samarqand"
#1 Yuqoridagi o'zgaruvchilarni jamlab, quyidagi ko'rinishda konsolga chiqaring:
print(kocha+" ko'chasi, "+ mahalla+" mahallasi, "
      +tuman +" tumani, "+viloyat+" viloyati.")
#2 Yuqoridagi o'zgaruvchilarning (kocha, mahalla, tuman, viloyat) qiymatini foydalanuvchidan so'rang. Va avvalgi mashqni takrorlang
#print("Qo'yidagi savollarga javob bering:")
# kocha=input("Ko'changiz:")
# mahalla=input("Mahallangiz:")
# tuman=input("Tumaningiz:")
# viloyat=input("Viloyatingiz:")
#print(kocha+" ko'chasi,\n"+ mahalla+" mahallasi,\n"+tuman +" tumani,\n"+viloyat+" viloyati.")
manzil=f"{kocha} ko'chasi, {mahalla} mahallasi, {tuman} tumani, {viloyat} viloyati"
print(manzil.upper())
print(manzil.lower())
print(manzil.title())
print(manzil.capitalize())
