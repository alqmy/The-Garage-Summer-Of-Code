import csv

username = input("Enter your username: ")
password = input("Enter your password: ")

with open("./users.csv", mode="r") as db:
    reader = csv.DictReader(db, fieldnames=["user", "password"])
    user = None

    for row in reader:
        if row["user"] == username:
            user = row
    
    if user:
        if user["password"] == password:
            print("Logged in!")
        else:
            print("Username or password incorrect")
    else:
        print("Username or password incorrect")
