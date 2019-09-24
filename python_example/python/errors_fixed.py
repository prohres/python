import sys

filename = "files/user_name.txt"

print("=====START=====")


while True:
    try:
        print("Inside TRY")
        myfile = open(filename, mode='r', encoding='latin_1')
    except Exception:
        print("Inside EXCEPT")
        print("Error Found!")
        print(sys.exc_info()[1])
        filename = input("Enter file name: ")
    else:
        print("Inside ELSE")
        print(myfile.read())
        myfile.close()
        sys.exit()
    # finally:
    #     print("Inside FINALLY")


print("=====FINISH=====")
