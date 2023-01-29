# # Foydalanuvchidan juft son kiritishni so'rang. Agar foydalanuvchi juft son kiritsa "Rahmat!", agar toq son kiritsa
# # "Bu son juft emas" degan xabarni chiqaring.
# 
# a=int(input("Iltimos, juft son kiriting!\n>>>"))
# if a%2:
#     print("Kechurasiz, bu son juft emas!")
# else:
#     print("Rahmat!!")
#     
# # Foydalanuvchi yoshini so'rang, va muzeyga kirish uchun chipta narhini quyidagicha chiqaring:
# 
# # Agar foydalanuvchi 4 yoshdan kichkina yoki 60 dan katta bo'lsa bepul
# # Agar foydalanuvchi 18 dan kichik bo'lsa 10000 so'm
# # Agar foydalanuvchi 18 dan katta bo'lsa 20000 so'm
# 
# yosh=int(input("Yoshingiz nechida?\n>>>"))
# if yosh<=4 or yosh>=60:
#     narx="Kirish bepul"
# elif yosh<=18:
#     narx="Kirish 10000 so'm"
# else:
#     narx="Kirish 20000 so'm"
# print(f"Siz uchun {narx.lower()}.")
# 
# #Foydalanuvchidan ikita son kiritishni so'rang, sonlarni solishtiring va ularning teng yoki katta/kichikligi haqida
# # xabarni chiqaring
#   
# print("Iltimos, ikkita son kiriting!")
# a=int(input("1-son:"))
# b=int(input("2-son:"))
# if a==b:
#     print(F"{a}={b}")
# elif a<=b:
#     print(F"{a}<{b}")
# else:
#     print(F"{a}>{b}")
#     
# # mahsulotlar degan ro'yxat yarating va kamida 10 ta turli mahsulotni kiriting. Yangi, savat degan bo'sh ro'yxat
# # yarating va foydalanuvchidan savatga kamida 5 ta mahsulot kiritishni so'rang. Savatdagi elementlarni, mahsulotlar
# # ro'yxati bilan solishtiring va qaysi biri ro'yxatda bo'lsa "Mahsulot do'konimizda bor"
# # aks holda, "Mahsulot do'konimizda yo'q" degan xabarlarni chiqaring.
# 
mahsulotlar=['savzu','piyoz','pomidor','bodring','kartoshka','chesnok','non','makaron','guruch','yog\'']
savat=[]
savat.append(input('1-mahsulot:'))
savat.append(input('2-mahsulot:'))
savat.append(input('3-mahsulot:'))
savat.append(input('4-mahsulot:'))
savat.append(input('5-mahsulot:'))
if savat:
    for tovar in savat:
        if tovar.lower() in mahsulotlar:
            print(f"{tovar.title()} do'konimizda bor!")
        else:
            print(f"{tovar.title()} do'konimizda yo'q!")
else:
    print("Savatchangiz bo'sh")
# # Yuqoridagi dasturni quyidagicha o'zgartiring: foydalanuvchidan 5 ta mahsulot kiritishni so'rang.
# # Foydalanuvchi so'ragan va do'konda bor mahsulotlarni yang, bor_mahsulotlar degan ro'yxatga, do'konda yo'q
# # mahsulotlarni esa mavjud_emas degan ro'yxatga qo'shing. Agar mavjud_emas ro'yxati bo'sh bo'lsa, "Siz so'ragan
# # barcha mahsulotlar do'konimizda bor" degan xabarni, aks holda esa "Quyidagi mahsulotlar do'konimizda yo'q: ....."
# # degan xabarni chiqaring.
#       
# 
# mahsulotlar=['sabzi','piyoz','pomidor','bodring','kartoshka','chesnok','non','makaron','guruch','yog\'']
# savat=[]
# bor_mahsulotlar=[]
# mavjud_emas=[]
# for n in range(5):
#   savat.append(input(f"{n+1}-mahsulotni kiriting:"))
# for tovar in savat:
#         if tovar.lower() in mahsulotlar:
#             bor_mahsulotlar.append(tovar.lower())
#         else:
#             mavjud_emas.append(tovar.lower())
# 
# if mavjud_emas:
#     print("Quyidagi mahsulotlar do'konimizda yo'q")
#     for tovar in mavjud_emas:
#         print(tovar)
# else:
#     print("Siz so'ragan barcha mahsulotlar do'konimizda bor")
#     
# # foydalanuvchilar degan ro'yxat tuzing, va kamida 5 ta login qo'shing. Foydalanuvchidan yangi login tanlashni
# # so'rang va foydalanuvchi kiritgan loginni foydalanuvchilar degan ro'yxatning tarkibi bilan solishtiring. Agar
# # ro'yxatda bunday login mavjud bo'lsa, "Login band, yangi login tanlang!" aks holda "Xush kelibsiz, foydalanuvchi!"
# # xabarini chiqaring.
# 
# foydalanuvchilar=['azizjon','samandar','shohruz','sherxan','ozodbek']
# login=input("Yangi login tanlang:")
# if login.lower() in foydalanuvchilar:
#     print("Login band, yangi login tanlang!")
# else:
#     print("Xush kelibsiz, foydalanuvchi!")
#   
# Foydalanuvchidan biror butun son kiritishni so'rang. Foydalanuvchi kiritgan sonni 2 dan 10 gacha bo'lgan sonlardan
# qay biriga qoldiqsiz bo'linishini konsolga chiqaring.
# son=int(input("Bironta butun son kiriting:"))
# k_son=[]
# n_son=[]
# for n in range(2,11):
#     if son%n:
#         n_son.append(n)
#     else:
#         k_son.append(n)
# print(f"{son} soni {k_son} sonlariga qoldiqsiz bo'linadi")
#     
#     
#     
#     
