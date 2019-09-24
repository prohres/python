
import re
import json

filename = "files/data_users.json"
inputfile = open(filename, mode='r')

mytext = inputfile.read()

# \d = Digit [0-9]
# \D = non DIGIT
# \w = Alphabet symbol [A-Z, a-z]
# \W = non Alphabet symbol
# \s = breakspace
# \S = non breakspase
# [0-9]{4} = '2020'
# [A-Z][a-z]+ = 'Hilary'

textsearch = r"\w+\.\w+@\w+\.\w+"
allresult = re.findall(textsearch, mytext)

print(allresult)



