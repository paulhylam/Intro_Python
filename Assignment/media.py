import webbrowser


class Movie():
    # Class Movie is the blueprint for each movie
    # defining constructor which will collect the information


    def __init__(self, movie_title, movie_storyline,
                 movie_poster, trailer_youtube):
                 self.title = movie_title
                 self.storyline = movie_storyline
                 self.poster_image_url = movie_poster
                 self.trailer_youtube_url = trailer_youtube

    VALID_RATINGS = ["G", "PG", "PG-13", "R"]
    # Class variable which allows accesses by instances
    # UPPERCASE for CONSTANTS

    # defining an instance method to show the trailers
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)


# self is the object being created
# we want init function to remember the information of the movie
# 2 underscores for _ _ init _ _
# toy_story = media.Movie("Toy Story", "Toys Come to Life", ...)
#     __init__ gets called
#     self = toy_story                        ----->     toy_story
#     movie_title = "Toy Story"               ----->     title = "Toy Story"
#     movie_storyline = "Toys come to life"   ----->     movie_storyline = "Toys come to life"
#     toy_story.title = "Toy Story"
# https://google.github.io/styleguide/pyguide.html will help to guide the best practice of styling