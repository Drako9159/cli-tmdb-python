class Movie():
    def __init__(self):
        self.title = ""
        self.release_date = ""
        self.vote_average = 0.0
    
    def set_title(self, title):
        self.title = title
        return self
    
    def set_release_date(self, release_date):
        self.release_date = release_date
        return self
    
    def set_vote_average(self, vote_average):
        self.vote_average = vote_average
        return self
    
    def __str__(self):
        return f"{self.title} - {self.release_date} - RATING: {self.vote_average}"

def json_to_movie(json : dict) -> list[Movie]:
    movies = []
    for movie in json["results"]:
        m = Movie()
        m.set_title(movie["title"])
        m.set_release_date(movie["release_date"])
        m.set_vote_average(movie["vote_average"])
        movies.append(m)
    return movies
