# *********************9 dars************************************
# 
# 1 misol
# ismlar = ['wurik', 'ivan', 'nodir', 'azam', 'ravwan']
# for name in ismlar:
#     print(f"Salom dustim, {name}. Qayerdasan?")

# 2 misol
# print(f"Kod {len(ismlar)} marta takrorlandi")

# 3 misol
# sonlar = list(range(21, 100, 2))
# for son in sonlar:
#     print(son**3)

# 4 misol
# films = []
# print("7 ta eng sevimli filmingiz qaysilar?")
# for f in range(7):
#     films.append(input(f"{f+1} kino: "))
# print(films)

# 5 misol
# odamlar = int(input("Bugun nechta odam bilan kuriwdingiz? \n>>>"))
# kimlar = []
# for k in range(odamlar):
#     kimlar.append(input(f"{k+1}-kuriwgan odamingiz kim?: "))
# print(kimlar)


# *********************10 dars************************************

# 1 misol
# cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia']
# for car in cars:
#     if car == 'gm':
#        print(car.upper())
#     else:
#         print(car.title())

# 2 misol
# cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia']
# for car in cars:
#     if car != 'gm':
#         print(car.title())
#     else:
#         print(car.upper())


# login = input("loginni kiriting: ")
# if login.lower() == 'admin':
#     print("Xuw kelibsiz janob admin, foydalanuvcilar ruyxatini kurasizmi?")
# else:# 3 misol
#     print(f"Xush kelibsiz, {login.title()}!")
              
# 4 misol
# son1 = float(input("1-sonni kiriting: "))
# son2 = float(input("2-sonni kiriting:"))
# if son1 == son2:
#     print("sonlar teng")
# else:
#     print("Xayr")

# 5 misol
# son = float(input("ixtiyoriy son kiriting: "))
# if son < 0:
#     print("son manfiy")
# else:
#     print("son musbat")

# 6 misol
# son = float(input('Ixtiyoriy son kiriting: '))
# print(son**(1/2)) if son>0 else print('Musbat son kiriting')


# *********************11 dars************************************
# 1 misol
# son = float(input("Juft son kiriting: "))
# if son%2:
#     print('Son juft emas.')
# else:
#     print("Ajoyib!")

# 2 misol
# yow = int(input("Yowingiz nechida? >>>"))
# if yow<=4 or yow>=60:
#     narx = 0;
# elif yow < 18:
#     narx = 10000
# else:
#     narx = 20000
# print(f"Chipta {narx} so'm")

# 3 misol
# s1 = float(input("1-sonni kiriting: "))
# s2 = float(input("2-sonni kiriting: "))
# if s1==s2:
#     print(f"{s1}={s2}")
# elif s1<s2:
#     print(f"{s1}<{s2}")
# else:
#     print(f"{s1}>{s2}")

# 4 misol
# maxsulotlar = ['wakar', "tuz'", "sovun", 'tuxum', 'piyoz',
#                'sabzi', 'olma', 'banan', 'uzum', 'qovun']
# savat = []
# for k in range(6):
#     savat.append(input(f"Savatga {k+1}-maxsulotni qo'shing: "))
# for maxsulot in savat:
#     if maxsulot in maxsulotlar:
#         print(f"dukonda {maxsulot} bor")
#     else:
#         print(f"dukonda {maxsulot} yuq")

# 5 misol
# maxsulotlar = ['wakar', "tuz'", "sovun", 'tuxum', 'piyoz',
#              'sabzi', 'olma', 'banan', 'uzum', 'qovun']

# savat = []
# for k in range(5):
#     savat.append(input(f"Savatga {k+1}-maxsulotni quwing: "))

# bor_maxsulotlar = []
# mavjudmas = []
# for maxsulot in savat:
#     if maxsulot in maxsulotlar:
#         bor_maxsulotlar.append(maxsulot)
#     else:
#         mavjudmas.append(maxsulot)

# if mavjudmas:
#   print(f"Do'konimizda quyidagi maxsulotlar yuq:")
#   for maxsulot in mavjudmas:
#     print(maxsulot)
# else:
#   print("Siz so'ragan barcha maxsulotlar do'konimizda bor")

# 6 misol
# users = ['wurik','sabrina','imona','umid', 'nortoy']
# login = input("Yangi login kiriting: >>>")
# if login in users:
#     print('Login band, yangi login tanlang!')
# else:
#     print(f"Xuw kelibsiz, {login.title()}!")

# 7 misol
# son = int(input("Istalgan butun son kiriting: "))
# for k in range(3,9):
#     if not (son%k):
#         print(f"{son} soni {k} ga qoldiqsiz bulinadi")