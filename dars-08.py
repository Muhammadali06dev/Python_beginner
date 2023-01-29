# O'zingizga ma'lum davlatlarning ro'yxatini tuzing va ro'yxatni konsolga chiqaring.
davlatlar=['Rossiya','Italiya','AQSH','Kanada','Chili']
print(davlatlar)

# Ro'yxatning uzunligini konsolga chiqaring
print(len(davlatlar))

# sorted() funktsiyasi yordamida ro'yxatni tartiblangan holda konsolga chiqaring
print(sorted(davlatlar))

#  sorted() yordamida ro'yxatni teskari tartibda konsolga chiqaring
print(sorted(davlatlar, reverse=True))

#  Asl ro'yxatni qaytadan konsolga chiqaring
print(davlatlar)

# reverse() metodi yordamida ro'yxatni ortidan boshlab chiqaring
davlatlar.reverse()

# sort() metodi yordamida ro'yxatni avval alifbo bo'yicha, keyin esa alifboga teskari tartibda konsolga chiqaring.
davlatlar.sort()
print(davlatlar)
davlatlar.sort(reverse=True)
print(davlatlar)

# 120 dan 1200 gacha bo'lgan juft sonlar ro'yxatini tuzing
juft_sonlar=list(range(120,1202,2))
print(juft_sonlar)

# Ro'yxatdagi sonlar yig'indisini hisoblang va konsolga chiqaring
print(sum(juft_sonlar))

# Ro'yxatdagi eng katta va eng kichik son o'rtasidagi ayirmani hisoblang va konsolga chiqaring
print(max(juft_sonlar)-min(juft_sonlar))

# Ro'yxatdagi elementlar sonini hisoblang
print(len(juft_sonlar))

# Ro'yxatning boshidan, o'rtasidan va oxiridan 20 ta qiymatni konsolga chiqaring
print(juft_sonlar[:20])
print(juft_sonlar[-20:])
print(juft_sonlar[520:541])

# taomlar degan ro'yxat yarating va ichiga istalgan 5ta taomni kiriting
taomlar=['osh','shurva','shashlik','manti','makaron']

# nonushta degan yangi ro'yxatga taomlardan nusxa oling
nonushta=taomlar[:]
nonushta.remove('makaron')
nonushta.remove('shashlik')
nonushta.append("choyu nun")
nonushta.append("qoqak")