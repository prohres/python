
names = ['Sem', 'Piter', 'Rob', 'Ben', 'Jhon']

print(names)
print(len(names))
print(names[2])

names.append("Rick")

print(names)

names.insert(3, "Pit")
print(names)

del names[0]
print(names)

names.remove("Pit")
print(names)

del_names = names.pop()
print("Deleted names is:" + del_names)
print(names)

names.sort()
print(names)

