class Movie:
    def __init__(self, title, genre, length, cast, director, adminRating, language, capacity):
        self.title = title
        self.genre = genre
        self.length = length
        self.cast = cast
        self.director = director
        self.adminRating = adminRating
        self.language = language
        self.capacity = int(capacity)
        self.showTiming = [("8:00", "10:00"), ("10:30", "12:30"), ("1:00", "3:00")]
        self.userRating = adminRating
        self.bookedSeats = 0
        self.avgUserRating = self.adminRating

    def showAvailableSeats(self):
        self.showsAndCapacity = {"8:00-10:00": self.capacity, "10:30-12:30": self.capacity, "1:00-3:00": self.capacity}
        return self.showsAndCapacity

    def getAvgUserRating(self):
        return self.avgUserRating

    def calculateAvgUserRating(self):
        self. avgUserRating = (self.avgUserRating + self.userRating) / 2

    def setUserRating(self, rating):
        self.userRating = rating
        self.calculateAvgUserRating()



