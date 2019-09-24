

name = input("Plase enter Your name: ")
print("Hello " + name + "!")

num_x = input("Enter X: ")
num_y = input("Enter X: ")

suma = int(num_x) + int(num_y)
print(suma)

massage = ""
while True:
    massage = input("Password: ")
    if massage == 'good':
        break
    print(massage + " Pasword not correct")

print("Pasword was: " + massage)


mylist = []
msg = ""

while msg != 'stop'.upper():
    msg = input("Enter new item, and STOP to finish ")
    mylist.append(msg)
    print(msg)

print(mylist)

