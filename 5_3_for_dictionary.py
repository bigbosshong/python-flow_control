person = {'name': 'bigboss', 'address': 'Seoul', 'interest':'Web' }
print(person['name'])

for key in person:
    print(key, person[key])

persons = [
    {'name': 'bigboss', 'address': 'Seoul', 'interest':'Web' },
    {'name': 'hong', 'address': 'Uiwang', 'interest':'Game' },
    {'name': 'hoya', 'address': 'Jeju', 'interest':'Cafe' }
]

for person in persons:
    for key in person:
        print(key, ':', person[key])
    print('---------------------------------------------')
