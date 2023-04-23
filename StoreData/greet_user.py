import json

def greet_user():
    """Greet the user by name"""
    filename = "username.json"
    try:
        with open(filename) as f:
            username = json.load(f)
            print(f"Welcome back, {username}")
    except FileNotFoundError:
        username = input("What is your name?: ")
        with open(filename, "w") as f:
            json.dump(username, f)
            print(f"We'll remember you when you come back, {username}")
            
greet_user()