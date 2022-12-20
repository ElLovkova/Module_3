import json

password = {}

def login_function(login, passwd):
    with open('auth.json', 'r') as f:
        password = json.load(f)
    if (login in password.keys() and password[login] == passwd):
        print("Ok")
    elif (login in password.keys() and password[login] != passwd):
        print("Password incorrect")
    else:
        print("Login incorrect")



login = input("login: ")
passwd = input("password: ")
login_function(login, passwd)