
import json

filename = "files/user_setings.json"
myfile = open(filename, mode='w', encoding='latin_1')

player1 = {
    'PlayerName': 'kozak',
    'Score': 345,
    'Awards': ["USD", "USD", "GBP"]
}

player2 = {
    'PlayerName': 'sotnuk',
    'Score': 346,
    'Awards': ["RUB", "CAD", "PLN"]
}

myplayers = []
myplayers.append(player1)
myplayers.append(player2)

# ---------- SAVE by JSON ----------------

json.dump(myplayers, myfile)
myfile.close()

# ---------- LOAD by JSON ----------------

myfile = open(filename, mode='r', encoding='latin_1')
json_data = json.load(myfile)

for user in json_data:
    print("Player Name is: " + str(user['PlayerName']))
    print("Player Score is: " + str(user['Score']))
    print("Player Awards #1: " + str(user['Awards'][0]))
    print("Player Awards #2: " + str(user['Awards'][1]))
    print("Player Awards #3: " + str(user['Awards'][2]))
    print("-------------------------------------------")