users = [{'name': 'Caspar', 'age': '23', 'location': '57.107118, 12.2520907', 'favourite color': 'blue', 'gmail': 'caspar@work.com', 'password': 'unicorns'},
         {'name': 'Philip', 'age': '42', 'location': '59.33258, 18.0649',
             'favourite color': 'green', 'gmail': 'philip@work.com', 'password': 'apples'},
         {'name': 'Johan', 'age': '23', 'location': '58.41086, 15.62157',
             'favourite color': 'red', 'gmail': 'johan@work.com', 'password': 'boomerangs'},
         {'name': 'Jessica', 'age': '26', 'location': '56.67446, 12.85676',
          'favourite color': 'green', 'gmail': 'jessica@work.com', 'password': 'duck'},
         {'name': 'Olle', 'age': '30', 'location': '57.107111,12.2520950', 'favourite color': 'pink', 'gmail': 'olle@work.com', 'password': 'donkey'}]
keys = ['name', 'age', 'location', 'favourite color', 'gmail', 'password']
user_dictionary = {}

for number, user in enumerate(users):
    user_dictionary[users[number]["name"]] = user
# print(user_dictionary)

for name, informations in user_dictionary.items():
    print(f"\n{name}{'-'*5}")
    for information in informations:
        print(information,informations[information])

users = {'Caspar': {'name': 'Caspar', 'age': '23', 'location': '57.107118, 12.2520907', 'favourite color': 'blue', 'gmail': 'caspar@work.com', 'password': 'unicorns'},
         'Philip': {'name': 'Philip', 'age': '42', 'location': '59.33258, 18.0649', 'favourite color': 'green', 'gmail': 'philip@work.com', 'password': 'apples'},
         'Johan': {'name': 'Johan', 'age': '23', 'location': '58.41086, 15.62157', 'favourite color': 'red', 'gmail': 'johan@work.com', 'password': 'boomerangs'},
         'Jessica': {'name': 'Jessica', 'age': '26', 'location': '56.67446, 12.85676', 'favourite color': 'green', 'gmail': 'jessica@work.com', 'password': 'duck'},
         'Olle': {'name': 'Olle', 'age': '30', 'location': '57.107111,12.2520950', 'favourite color': 'pink', 'gmail': 'olle@work.com', 'password': 'donkey'}
         }
print(users["Olle"])
