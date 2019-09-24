
curency_code = ['usd', 'eur', 'gbp', 'rub', 'cad', 'pln', 'sek', 'chf', 'czk', 'uah']
for x in curency_code:
    print(x.upper())

number_list = list(range(0, 10))
for x in number_list:
    x = x * 2
    print(x)

number_list.sort(reverse=True)
print(number_list)

print("Max is: " + str(max(number_list)))
print("Min is: " + str(min(number_list)))
print("Sum is: " + str(sum(number_list)))

my_currency_code = curency_code[1:4]
print(my_currency_code)
my_currency_code = curency_code[:4]
print(my_currency_code)
my_currency_code = curency_code[-3:-1]
print(my_currency_code)

my_currency_code = curency_code[:]
print(my_currency_code)