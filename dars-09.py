# Kamida 5 elementdan iborat ismlar degan ro'yxat tuzing, va ro'yxatdagi har bir ismga takrorlanuvchi xabar yozing
ismlar=['Muhammadali','Azizjon','Samandar','Sherxan','Shohruz']
for ism in ismlar:
    print("Nagzimi", ism)
    
# Yuqoridagi tsikl tugaganidan so'ng, ekranga "Kod n marta takrorlandi" degan xabarni chiqaring (n o'rniga kod necha marta takrorlanganini yozing)
print(f"Kod {len(ismlar)} marta takrorlandi")

# 10 dan 100 gacha bo'lgan toq sonlar ro'yxatini tuzing. Ro'yxatning xar bir elementining kubini yangi qatordan konsolga chiqaring.
toq=list(range(11,100,2))
for kub in toq:
    print(f"{kub} ning kubi {kub**3} ga teng")
    
# Foydalanuvchidan 5 ta eng sevimli kinolarini kiritshni so'rang, va kinolar degan ro'yxatga saqlab oling. Natijani konsolga chiqaring.
kinolar=[]
print("5 ta eng sevimli kinolaringizni kiriting")
for n in range(5):
    kinolar.append(input(f"{n+1} - chi kinoni kiriting:"))
print(kinolar)

# Foydalanuvchidan bugun nechta odam bilan uchrashganini (suhbatlashganini) so'rang, va har bir suhbatlashgan odamning ismini birma-bir so'rab ro'yxatga yozing. Ro'yxatni konsolga chiqaring.
odam=[]
n=int(input("Bugun nechta odam bilan uchrashdigingiz?\n>>>"))
for a in range(n):
    odam.append(input(f"{a+1}-odamni kiriting:"))
print(odam)    