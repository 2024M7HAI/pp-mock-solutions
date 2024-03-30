# You'd want to put all classes in separate Python files, but I put them in one for the sake of brevity

# Task 1: Class & constructor
class MusicItem:

    def __init__(self, title, artist, release_year, genre):
        self.title = title
        self.artist = artist
        self.release_year = release_year
        self.genre = genre
        self.age = None

    # Task 2: Argument & class attribute
    def calculate_age(self, year):
        self.age = year - self.release_year

    # Task 3: Magic Method & Comparisons
    def __eq__(self, other):
        return self.title == other.title and self.artist == other.artist


# Task 4: Subclass "Album"
class Album(MusicItem):
    # Inherit constructor and add tracks
    def __init__(self, title, artist, release_year, genre, tracks):
        super().__init__(title, artist, release_year, genre)
        self.tracks = tracks

# Task 5: Subclass "Single"
class Single(MusicItem):
    # Inherit constructor and add duration
    def __init__(self, title, artist, release_year, genre, duration):
        super().__init__(title, artist, release_year, genre)
        self.duration = duration

    # Provide an appropriate string representation:
    def __str__(self):
        return f"Single Title: {self.title}, Artist: {self.artist}, Year: {self.release_year}, Genre: {self.genre}, Duration: {self.duration}s"


# Example usage (not required for the answer, but included for clarity here)
# What a banger! https://youtu.be/dQw4w9WgXcQ?si=UptjJ-ZVivD9nwI1
rick_roll = Single("Never Gonna Give You Up", "Rick Astley", 1987, "Pop", 213)
rick_roll.calculate_age(2024)
print(rick_roll)
print(rick_roll.age)