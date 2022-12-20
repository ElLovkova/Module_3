import json

password = {}

def register(login, passwd):
    with open('auth.json', 'r') as f:
        password = json.load(f)
    if login not in password.keys():
        password[login] = passwd
        with open('auth.json', 'w') as f:
            json.dump(password, f)
    else:
        print("Login exists")




login = input("login: ")
passwd = input("password: ")
register(login, passwd)

