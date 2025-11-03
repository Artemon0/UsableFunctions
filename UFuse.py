from UsableFunctions.UF import UsableFunctions as u

usersM = [{'name': 'Artem', 'password': '1234', 'id': 1}]
user = {'name': 'Artem', 'password': '1234', 'id': 1}
print(u.users(usersM, user))
print(u.register(usersM, user))