
users = []
def create_record(name, phone, address):
    record = {
        'name': name,
        'phone': phone,
        'address': address
    }
    users.append(record)


user1 = create_record("Sem", "+38097", "Lviv")
user2 = create_record("Ben", "+38096", "Dnipro")
user3 = create_record("Leo", "+38068", "Poltava")

print(users)

def give_award(medal, *persons):
    for person in persons:
        print("Mister " + person.title() + " give " + medal)


give_award("MTV", "Ben", "Sem")
give_award("Oscar", "Pit", "Rob")