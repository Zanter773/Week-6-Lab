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

if username in data:
    print("true")
    password = input("What is your password? \n")
    if password in data[username]:
        print("true")