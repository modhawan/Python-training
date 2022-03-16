from bookMyShow.MyException import MyException


class User:
    def __init__(self, theater):
        self.theater = theater
        self.showMenu()

    def showMenu(self):
        try:
            print("***** Welcome User *****")
            movieList = self.theater.items()
            for idx, val in enumerate(movieList):
                print(idx, end=". ")
                print(val[0])
            n = int(input("Choose a movie."))
            movieWithTitle = movieList[n]
            movie = movieWithTitle[1]
            print("Title: ", movie.title)
            print("Genre: ", movie.genre)
            print("Length: ", movie.length)
            print("Cast: ", movie.cast)
            print("Director: ", movie.director)
            print("Language: ", movie.language)
            print("Admin Rating: ", movie.adminRating)
            print("Timings: ", movie.showTiming)
            print("User Rating: ", movie.userRating)
            print("****************************")
            print("1. Book Tickets")
            print("2. Cancel Tickets")
            print("3. Give User Rating")
            inp = int(input("Choose the option"))
            if(inp == 1):
                self.bookTickets(movie)
            elif(inp == 2):
                self.cancelTickets(movie)
            elif(inp == 3):
                self.giveUserRating(movie)
            else:
                raise MyException("Choose valid option")
        except ValueError as e:
            print(e)
        except MyException as e:
            print(e)
        except Exception as e:
            print(e)

    def bookTickets(self, movie):
        try:
            print("Showing available seats")
            seats = movie.showAvailableSeats()
            showsList = seats.items()
            for idx, val in enumerate(showsList):
                print(idx, end=": ")
                print(val[0], val[1])
            inp = int(input("Choose the show"))
            tickets = input("Enter number tickets for booking: ")
            if(showsList[inp][1] >= tickets):
                if(inp == 0):
                    movie.showsAndCapacity["8:00-10:00"] -= tickets
                elif(inp == 1):
                    movie.showsAndCapacity["10:30-12:30"] -= tickets
                elif(inp == 2):
                    movie.showsAndCapacity["1:00-3:00"] -= tickets
                else:
                    raise MyException("Choose the show correctly")
            else:
                raise MyException("Tickets are not available")
        except MyException as e:
            print(e)
        except Exception as e:
            print(e)

    def cancelTickets(self, movie):
        try:
            seats = movie.showAvailableSeats()
            showsList = seats.items()
            for idx, val in enumerate(showsList):
                print(idx, end=": ")
                print(val[0], val[1])
            inp = int(input("Choose the show"))
            cancelTicketNum = input("Enter number tickets for canceling: ")
            if(showsList[inp][1]+cancelTicketNum > movie.capacity):
                if(inp == 0):
                    movie.showsAndCapacity["8:00-10:00"] += cancelTicketNum
                elif(inp == 1):
                    movie.showsAndCapacity["10:30-12:30"] += cancelTicketNum
                elif(inp == 2):
                    movie.showsAndCapacity["1:00-3:00"] += cancelTicketNum
                else:
                    raise MyException("Choose the show correctly")
            else:
                raise MyException("Your are doing something wrong")
        except MyException as e:
            print(e)
        except Exception as e:
            print(e)

    def giveUserRating(self, movie):
        rating = input("Enter the user rating")
        movie.setUserRating(rating)
