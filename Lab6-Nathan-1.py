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
            attempts -= 1
            print(f"Incorrect Password. {attempts} attempt(s) remaining.")
            if attempts == 0:
                print("Too many incorrect passwords. Account Locked.")
else:
    print("User not found. Exiting.")