class Media:
    def play(self):
        return "Media ijro qilinmoqda..."

class Song(Media):
    def __init__(self, title, artist):
        self.title = title
        self.artist = artist

    def play(self):
        return f"Qoshiq ijro qilinmoqda: '{self.title}' by {self.artist}"

class Movie(Media):
    def __init__(self, title, director):
        self.title = title
        self.director = director

    def play(self):
        return f"Film ijro qilinmoqda: '{self.title}' (Rejissor: {self.director})"

class Podcast(Media):
    def __init__(self, title, host):
        self.title = title
        self.host = host

    def play(self):
        return f"Podcast tinglanmoqda: '{self.title}' by {self.host}"


media_list = [
    Song("Bilaman", "Sevinch Mominova"),
    Movie("Interstellar", "Christopher Nolan"),
    Podcast("Python Darslari", "Jahongir")
]

for media in media_list:
    print(media.play())
