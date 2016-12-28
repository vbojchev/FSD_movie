import webbrowser

class Movie():
    """in the media I'm declaring all needed things"""
    VALID_RAITINGS = ["G","PG","PG13","R"]
    # definining the contstructor of the class
    def __init__(self, movie_title, movie_storyline, poster_image, movie_trailer):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = movie_trailer

#  show_trailer uses webbrower's open function to open the trailer in a new window  
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
        
        
