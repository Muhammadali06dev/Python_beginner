# Yangi cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia'] degan ro'yxat tuzing, ro'yxat elementlarining birinchi harfini katta qilib konsolga chqaring. GM uchun ikkala harfni katta qiling.
cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia']
for car in cars:
    if car == "gm":
        print(car.upper())
    else:
        print(car.title())

# Yuqoridagi mashqni teng emas (!=) operatori yordamida bajaring.
for car in cars:
   if car != "gm":
      print(car.title())
   else:
       print(car.upper())

# Foydalanuvchi login ismini so'rang. Agar login admin bo'lsa, "Xush kelibsiz, Admin. Foydalanuvchilar ro'yxatini
# ko'rasizmi?" xabarini konsolga chiqaring. Aks holda, "Xush kelibsiz, {foydalanuvchi_ismi}!" matnini konsolga
# chiqaring.
login=input("Iltimos, login ismingizni kiriting:")
if login.lower() == 'admin':
    print("Xush kelibsiz, Admin. Foydalanuvchilar ro'yxatini ko'rasizmi?")
else:
    print(f"Xush kelibsiz, {login.title()}")
    
# Foydalanuvchidan 2 ta son kiritishni so'rang. Agar ikki son bir-biriga teng bo'lsa, "Sonlar teng" ekan degan yozuvni konsolga chiqaring.
print("Iltimos, 2 ta son kiriting")
a=float(input("1-son:"))
b=float(input("2-son:"))
if a==b:
 print("sonlar teng!")
else:
    print("raxmat!")
    
# Foydalanuvchidan istalgan son kiritishni so'rang. Agar son manfiy bo'lsa konsolga "Manfiy son", agar musbat bo'lsa "Musbat son" degan xabarni chiqaring.
a=float(input("Istalgan soningizni kiriting:"))
if a >= 0:
    print("Musbat son!")
else:
    print("Manfiy son!")
    
# Foydalanuvchidan son kiritishni so'rang, agar son musbat bo'lsa uning ildizini hisoblab konsolga chiqaring. Agar son manfiy bo'lsa, "Musbat son kiriting" degan xabarni chiqaring.
a=float(input("Istagan soningizni kiriting:"))
if a >=0:
        print(f"{a} ning ildizi {a**(1/2)} ga teng")
else:
        print("Iltimos, musbat son kiriting")