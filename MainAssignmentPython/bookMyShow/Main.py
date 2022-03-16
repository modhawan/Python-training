import sys

from bookMyShow.Admin import Admin
from bookMyShow.Person import Person
from bookMyShow.User import User

# ----- Global dictionary for storing values ------
class Main:
    def __init__(self):
        self.theater = {}
        self.userCredentials = {"admin": "password@123", "user1": "password1", "user2": "password2"}


    def login(self):
        print("***** Welcome to BookMyShow *****")
        try:
            username = input("Username: ").lower()
            password = input("Password: ")
            if (username in self.userCredentials):
                if(username == "admin" and self.userCredentials.get(username) == password):
                    obj = Admin(self.theater)
                elif(self.userCredentials.get(username) == password):
                    obj = User(self.theater)
                else:
                    raise MyException("Incorrect username and password!!!")
            else:
                raise MyException("User does not exist!!!")
        except MyException as e:
            print(e)
        except Exception as e:
            print(e)


    def register(self):
        print("***** Create new Account *****")
        username = input("Name: ").lower()
        email = input("Email: ").lower()
        phone = input("Phone: ")
        age = input("Age: ")
        password = input("Password: ")
        try:
            if(username not in self.userCredentials):
                obj = Person(username, email, phone, age, password)
                self.userCredentials[username] = obj
            else:
                raise MyException("Username already exists")
        except MyException as e:
            print(e)
        except Exception as e:
            print(e)

    def start(self):
        print("***** Welcome to BookMyShow *****")
        print("1. Login")
        print("2. Register new account")
        print("3. Exit")
        try:
            n = int(input("Enter your choice: "))
            if (n == 1):
                self.login()
            elif (n == 2):
                self.register()
            else:
                sys.exit(0)
        except ValueError:
            print("Please enter numeric value")


if __name__ == "__main__":
    app = Main()
    app.start()
