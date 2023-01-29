# Foydalanuvchidan juft son kiritishni so'rang. Agar foydalanuvchi juft son kiritsa "Rahmat!",
# agar toq son kiritsa "Bu son juft emas" degan xabarni chiqaring.
son=int(input("Iltimos, juft son kiriting:"))
if son%2:
    print("Bu son juft emas!!!")
else:
    print("Rahmat!")
    
# Foydalanuvchi yoshini so'rang, va muzeyga kirish uchun chipta narhini quyidagicha chiqaring:
# 
# Agar foydalanuvchi 4 yoshdan kichkina yoki 60 dan katta bo'lsa bepul
# Agar foydalanuvchi 18 dan kichik bo'lsa 10000 so'm
# Agar foydalanuvchi 18 dan katta bo'lsa 20000 so'm

yosh=int(input("Yoshingizni kiriting:"))
if yosh < 4 or yosh > 60:
    narx=0
elif yosh<18:
    narx=10000
else:
    narx=20000
print(f"Siz uchun kirish narxi {narx} so'm!")

# Foydalanuvchidan ikita son kiritishni so'rang, sonlarni solishtiring va
# ularning teng yoki katta/kichikligi haqida xabarni chiqaring
print("Iltimos ikkita son kiriting:")
a=int(input("1-son:"))
b=int(input("2_son:"))
if a>b:
    print(f"{a}>{b}")
elif a<b:
    print(f"{a}<{b}")
else:
    print(f"{a}={b}")

# mahsulotlar degan ro'yxat yarating va kamida 10 ta turli mahsulotni kiriting. Yangi, savat degan bo'sh ro'yxat yarating
# va foydalanuvchidan savatga kamida 5 ta mahsulot kiritishni so'rang. Savatdagi elementlarni,
# mahsulotlar ro'yxati bilan solishtiring va qaysi biri ro'yxatda bo'lsa "Mahsulot do'konimizda bor" aks holda,
# "Mahsulot do'konimizda yo'q" degan xabarlarni chiqaring.

mahsulotlar=['makaron','guruch','piyoz','sabzi','kartoshka','pomidor','chesnok','bodring','loviya','non']
savat=[]
for n in range(5):
    savat.append(input(f"{n+1}-mahsulotni kiriting:"))
for mahsulot in savat:
    if mahsulot.lower() in mahsulotlar:
        print(f"{mahsulot.title()} do'konimizda bor")
    else:
        print(f"{mahsulot.title()} do'konimizda yo'q")


# Yuqoridagi dasturni quyidagicha o'zgartiring: foydalanuvchidan 5 ta mahsulot kiritishni so'rang.
# Foydalanuvchi so'ragan va do'konda bor mahsulotlarni yang, bor_mahsulotlar degan ro'yxatga, do'konda yo'q
# mahsulotlarni esa mavjud_emas degan ro'yxatga qo'shing. Agar mavjud_emas ro'yxati bo'sh bo'lsa, "Siz so'ragan
# barcha mahsulotlar do'konimizda bor" degan xabarni, aks holda esa "Quyidagi mahsulotlar do'konimizda yo'q: ....."
# degan xabarni chiqaring.


mahsulotlar=['makaron','guruch','piyoz','sabzi','kartoshka','pomidor','chesnok','bodring','loviya','non']
savat=[]
bor_mahsulotlar=[]
mavjud_emas=[]

for n in range(5):
    savat.append(input(f"{n+1}-mahsulotni kiriting:"))
for mahsulot in savat:
    if mahsulot.lower() in mahsulotlar:
        bor_mahsulotlar.append(mahsulot.lower())
    else:
        mavjud_emas.append(mahsulot.lower())
if mavjud_emas:
    print("Quyidagi mahsulotlar do'konimizda yo'q:")
    for n in mavjud_emas:
        print(n.title())
else:
    print("Siz so'ragan barcha mahsulotlar do'konimizda bor")
# 
# foydalanuvchilar degan ro'yxat tuzing, va kamida 5 ta login qo'shing. Foydalanuvchidan yangi login tanlashni
# so'rang va foydalanuvchi kiritgan loginni foydalanuvchilar degan ro'yxatning tarkibi bilan solishtiring.
# Agar ro'yxatda bunday login mavjud bo'lsa, "Login band, yangi login tanlang!" aks holda "Xush kelibsiz,
# foydalanuvchi!" xabarini chiqaring.

foydalanuvchilar=['azizjon','samandar','shohruz','sherxan','ozod']
login=input("Yangi login tanlang:")
if login.lower() in foydalanuvchilar:
    print("Login band, yangi login tanlang!")
else:
    foydalanuvchilar.append(login.lower())
    print("Xush kelibsiz, foydalanuvchi!")

# Foydalanuvchidan biror butun son kiritishni so'rang. Foydalanuvchi kiritgan sonni 2 da 10 gacha bo'lgan
# sonlardan qay biriga qoldiqsiz bo'linishini konsolga chiqaring.

user=int(input("Bironta butun son kiriting:"))
for n in range(2,11):
    if not user % n:
        print(f"{user} {n} ga qoldiqsiz bo'linadi")

# 2-usul
kk=[]

user=int(input("Bironta butun son kiriting:"))
for n in range(2,11):
   if not user % n:
     kk.append(n)
print(f"{user} soni {kk} sonlariga qoldiqsiz bo'linadi")
        
