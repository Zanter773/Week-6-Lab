"""
Nathan Brooks
2/17/2025
User Login System
"""

userInfo = {"Nbrooks": "verysecurepass",
        "guest": "guest",
        "Mars": "starrynight",
        "Neptune": "blueorbital",
        }

username = input("What is your username? \n")
attempts = 3


if username in userInfo:
    while attempts > 0:
        password = input("What is your password? \n")
        if password == userInfo[username]:
            print(f'Welcome, {username}.')
            if username == 'guest':
                print("You have Guest access.")
                attempts = 0
            else:
                print("You have Security Level 1.")
                attempts = 0
        else:
            print(f"Incorrect Password. {attempts - 1} attempt(s) remaining.")
            attempts -= 1
else:
    print("User not found. Exiting.")