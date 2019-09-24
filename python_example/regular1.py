import re

inputs_filename = "files/data_users.json"
result_filename = "files/result.txt"


inputsfile = open(inputs_filename, mode='r')
resultfile = open(result_filename, mode='a')
mytext = inputsfile.read()

lookfor = r"[\w._-]+@[\w._-]+\.[\w.]+"

results = re.findall(lookfor, mytext)

for item in results:
    print(item)
    resultfile.write(item + "\n")


print("Total: " + str(len(results)))



