import webbrowser


class Movie():
    """ This class provides a way to store movie-related info """
    VALID_RATINGS = ['G', 'PG', 'PG-13', 'R']

    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube):
        """ initialize a movie instance with its title, storyline, poster and
            trailer """
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        """ open a Movie instance's trailer in the default web browser """
        webbrowser.open(self.trailer_youtube_url)


# Just a test procedure if this script is run on its own
if __name__ == '__main__':
    print(Movie.__name__)
    print(Movie.__doc__)
