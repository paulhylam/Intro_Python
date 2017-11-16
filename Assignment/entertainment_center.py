# This program contains the information and running codes

import media
import fresh_tomatoes

# Instances are created for each movie based on the class Movie

toy_story = media.Movie('Toy Story',
                        'A story of a boy and his toys that come to life',
                        'http://upload.wikimedia.org/wikipedia/en/1/13/'
                        'Toy_Story.jpg',
                        'https://www.youtube.com/watch?v=nCqtQLmJTl0')

avatar = media.Movie('Avatar',
                     'A marine on an alien planet',
                     'https://upload.wikimedia.org/wikipedia/en/b/b0/'
                     'Avatar-Teaser-Poster.jpg',
                     'https://www.youtube.com/watch?v=5PSNL1qE6VY')

school_of_rock = media.Movie('School of Rock',
                             'A marine on an alien planet',
                             'https://i.ytimg.com/vi/eAry-ZV_gfs/'
                             'movieposter.jpg',
                             'https://www.youtube.com/watch?v=yMvpJDbWX_c')

hunger_game = media.Movie('Hunger Game',
                          'A marine on an alien planet',
                          'https://images-na.ssl-images-amazon.com/images/'
                          'I/91ikvZgoHZL._SL1500_.jpg',
                          'https://www.youtube.com/watch?v=n-7K_OjsDCQ')

# This code will create the webpage.

movies = [toy_story, avatar, school_of_rock, hunger_game]
fresh_tomatoes.open_movies_page(movies)

# print(media.Movie.VALID_RATINGS)
# print(toy_story.storyline)
# print(avatar.storyline)
# calling instance methods
# avatar.show_trailer()
