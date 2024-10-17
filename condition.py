# is_hot = False
# is_cold = True

# if is_hot:
#     print("It's a hot day")
#     print('Drink plenty of water')
# elif is_cold:
#     print("Its a cold day")
#     print("Wear warm clothes")
# else:
#     print("It's a lovely day")

# print("Enjoy your day")


# num=int(input("Enter a number: "))
# print(type(num))

# price = 1000000
# good_credit = True
# no_credit = False

# if good_credit:
#    down_payment = 0.1 * price

# elif no_credit:
#     down_payment = 0.2 * price

# print(f"Down Pyament: ${down_payment}")

# has_high_income = True
# has_good_credit = False

# if has_high_income or has_good_credit:
#     print("Eligible for loan ")


# has_high_income = True
# has_criminal_record = False

# if has_high_income and not  has_criminal_record:
#     print("Eligible for loan ")

# temperature = 40

# if ( temperature > 30):
#     print("It's a hot day")
# else:
#     print("It's a pleasent day")


# name = 'varun'
# length = len(name)
# if length < 3:
#     print("Name must be at least 3 caracter")
# elif length > 50:
#     print("The maximum lenght for the name is 50 characaters")
# else:
#     print("You are good to go")


# weigth=float(input("weight:"))
# unit=input('(L)bs or (K)kg: ')

# if unit.upper() == "L":
#     con = weigth * 0.4
#     print(f"You are {con} kilos")
# else:
#     con = weigth // 0.4
#     print(f"you are {con} pound")


wieght = int(input("Weight: "))
unit = (input("(g)gram or m: "))

if unit.upper() == "G":
    con = wieght * 1000
    print(f"your weight is {con} grams")

else:
    con = wieght * 10000
    print(f"Your weight is {con} mg")

