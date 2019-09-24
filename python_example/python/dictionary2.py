
elem = {
    'loc_x': 70,
    'loc_y': 50,
    'color': 'green',
    'health': 100,
    'name': 'Poc',
    'image': ['usd', 'eur', 'gbp', 'rub', 'cad', 'pln', 'sek', 'chf', 'czk', 'uah']
}

all_elem = []
for x in range(0, 10):
    all_elem.append(elem.copy())
   
for elem in all_elem:
    print(elem)

all_elem[5]['health'] = 30
print(all_elem)

