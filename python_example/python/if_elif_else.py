
age = 15

if age <= 4:
    print("You are baby!")
elif age > 4 and age < 12:
    print("You are kid!")
elif age >= 12 and age < 19:
    print("You are teenager!")
else:
    print("You are old!")

code = ['usd', 'eur', 'gbp', 'rub', 'cad', 'pln', 'sek', 'chf', 'czk', 'uah']
my_code = ['eur', 'pln', 'sek', 'czk']

for x in code:
    if x in my_code:
        print(x.upper() + " in the list my_code")
    # else:
    #     print(x.upper() + " not in the list my_code")

