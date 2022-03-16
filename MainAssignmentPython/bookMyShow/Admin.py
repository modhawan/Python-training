import sys

from bookMyShow.MyException import MyException
from bookMyShow.Movie import Movie


class Admin:
    def __init__(self, theater):
        self.theater = theater
        self.showMenu()

    def showMenu(self):
        try:
            print("***** Welcome Admin *****")
            print("1. Add New Movie Info")
            print("2. Edit Movie Info")
            print("3. Delete Movies")
            print("4. Logout")
            inp = int(input("Enter your choice: "))
            if (inp == 1):
                self.addMovie()
            elif (inp == 2):
                self.editMovieInfo()
            elif (inp == 3):
                self.deleteMovie()
            elif (inp == 4):
                self.logout()
            else:
                raise MyException("Please enter correct choice")

        except ValueError as e:
            print(e)
        except MyException as e:
            print(e)
        except Exception as e:
            print(e)

    def addMovie(self):
        title = input("Title: ")
        genre = input("Genre: ")
        length = input("Length: ")
        cast = input("Cast: ")
        director = input("Director: ")
        adminRating = input("Admin Rating: ")
        language = input("Language: ")
        capacity = input("Capacity: ")
        self.theater[title] = Movie(title, genre, length, cast, director, adminRating, language, capacity)

    def editMovieInfo(self, title):
        movie = self.theater[title]
        print("1. Genre")
        print("2. Length")
        print("3. Cast")
        print("4. Director")
        print("5. Admin Rating")
        print("6. Language")
        try:
            n = int(input("Enter your choice to edit"))
            if(n == 1):
                movie.genre = input("Genre: ")
            elif(n == 2):
                movie.length = input("Length: ")
            elif(n == 3):
                movie.length = input("Cast: ")
            elif(n == 4):
                movie.length = input("Director: ")
            elif(n == 5):
                movie.adminRating = input("Admin Rating: ")
            elif(n == 6):
                movie.language = input("Language: ")

        except ValueError as e:
            print(e)

    def deleteMovie(self):
        title = input("Enter title of the movie: ")
        self.theater.pop(title)

    def logout(self):
        print("*** Thank You ***")
        print("*** Logging Out ***")
        sys.exit(0)
