
# myfilename = "files/user_names.txt"

# myfile = open(myfilename, mode='r', encoding='utf_8')

# for num, line in enumerate(myfile, 1):
#     if "Gavrilyuk" in line:
#         print("Line #:" + str(num) + " " + line.strip())

# -------------------------------------------------------

inputfile = "files/list_of_passwords.txt"
outputfile = "files/search_password.txt"

search_password = "kolya"

workfile = open(inputfile, mode='r', encoding='latin_1')
newworkfile = open(outputfile, mode='a', encoding='latin_1')

for num, line in enumerate(workfile, 1):
    if search_password in line:
        print("Line #:" + str(num) + " " + line.strip())
        newworkfile.write("Found password: " + line)

workfile.close()
newworkfile.close()

