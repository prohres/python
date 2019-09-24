name = input("Your name is: ")

def print_hello(name):
    print("Hello mister " + name)
    print("Hello sir " + name)


def print_goodbay(name):
    print("Goodbay mister " + name)
    print("Goodbay sir " + name)


print("===START===")
print_hello(name)
print("-----------")
print_goodbay(name)
print("===FINISH===")

def sum_numbers(x, y):
    print(x+y)

sum_numbers(24, 24)
print("========")

def factorial(x):
    answer = 1
    for i in range(1, x + 1):
        answer = answer * i
    return answer


print(factorial(3))
print(factorial(5))
