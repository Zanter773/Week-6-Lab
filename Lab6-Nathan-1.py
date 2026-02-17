"""
Nathan Brooks
2/17/2025
User Login System
"""

data = {"Nbrooks": "verysecurepass",
        "guest": "guest",
        "Mars": "starrynight",
        "Neptune": "blueorbital",
        }

username = input("What is your username? \n")
attempts = 3


if username in data:
    password = input("What is your password? \n")
    if password == data[username]:
        print(f'Welcome, {username}.')
        if username == 'guest':
            print("You have Guest access.")
        else:
            print("You have Security Level 1.")
    else:
        print("Incorrect Password.")
else:
    print("User not found. Exiting.")