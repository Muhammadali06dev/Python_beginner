# ismlar degan ro'yxat yarating va kamida 3 ta yaqin do'stingizning ismini kiriting:
ismlar=['Ibroimjon', 'Ruslan','Bojon','Islom']

# Ro'yxatdagi har bir do'stingizga qisqa xabar yozib konsolga chiqaring:
print("Salom" , ismlar[0].upper())
print("Chi gap" , ismlar[1].upper())
print("Nagzimi", ismlar[2].upper())
print("Bobimi", ismlar[3].upper())

# sonlar deb nomlangan ro'yxat yarating va ichiga turli sonlarni yuklang (musbat, manfiy, butun, o'nlik).
sonlar=[10 , -4 , 5 , 2.6]

# Yuqoridagi ro'yxatdagi sonlar ustida turli arifmetik amallar bajarib ko'ring. Ro'yxatdagi ba'zi
# sonlarning qiymatini o'zgartiring, ba'zilarini esa almashtiring.
print(sonlar[0]+sonlar[2])
print(sonlar[1]**10)
print(f"{sonlar[0]}-{sonlar[3]}=", sonlar[0]-sonlar[3])

sonlar[3]=4.5
sonlar[2]=sonlar[1]+24

# t_shaxslar va z_shaxslar degan 2 ta ro'yxat yarating va biriga o'zingiz eng ko'p hurmat qilgan
# tarixiy shaxslarning, ikkinchisiga esa zamonamizdagi tirik bo'lgan shaxslarning ismini kiriting.
t_shaxslar=['Amir Temur' , 'Alisher Navoiy' , 'Beruniy']
z_shaxslar=['Bill Gates' , 'Elon Mask' , 'Putin']

# Yuqoridagi ro'yxatlarning har biridan bittadan qiymatni sug'urib olib (.pop()), quyidagi
# ko'rinishda chiqaring
print("Men tarixiy insonlardan "+ t_shaxslar.pop(2)+" bilan, zamonaviy insonlardan esa "+ z_shaxslar.pop(0) + " bilan suhbatlashishni istardim.")

# friends nomli bo'sh ro'yxat tuzing va unga .append() yordamida 5-6 ta mehmonga chaqirmoqchi
# bo'lgan do'stlaringizni kiriting.
friends=[]
friends.append("Ibroimjon")
friends.append("Bojon")
friends.append("Islom")
friends.append("Ruslan")
friends.append("Dilxush")

# Yuqoridagi ro'yxatdan mehmonga kela olmaydigan odamlarni .remove() metodi yordamida o'chrib tashlang.
friends.remove("Dilxush")
print(friends)

# Ro'yxatning oxiriga, boshiga va o'rtasiga yangi ismlar qo'shing.
friends.insert(0, 'Raufjon')
friends.insert(-1, 'Muminjon')
friends.insert(2, 'Dilxush')
print(friends)

# Yangi mehmonlar deb nomlangan bo'sh ro'yxat yarating. .pop() va .append() metodlari yordamida
# mehmonga kelgan do'stlaringizning ismini friends ro'yxatidan sug'urib olib, mehmonlar ro'yxatiga qo'shing.
mehmonlar=[]
mehmonlar.append(friends.pop(1))
mehmonlar.append(friends.pop(2))
mehmonlar.append(friends.pop(2))
mehmonlar.append(friends.pop(3))
print(mehmonlar)
del mehmonlar[-1]