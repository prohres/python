
elem = {
    'loc_x': 70,
    'loc_y': 50,
    'color': 'green',
    'health': 100,
    'name': 'Poc',
}
print(elem)

print("Local X = " + str(elem['loc_x']))
print("Local Y = " + str(elem['loc_y']))
print("His name is: " + elem['name'])

elem['rank'] = 'Separ'
print(elem)

del elem['rank']
print(elem)

elem['loc_x'] = elem['loc_x'] + 40
elem['health'] = elem['health'] - 30
if elem['health'] < 80:
    elem['color'] = 'yelow'

print(elem)
print(elem.keys())
print(elem.values())
