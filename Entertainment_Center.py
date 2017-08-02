import fresh_tomatoes
import media

# This is where class Movie pulls the information for each instance.

robin_hood = media.Movie("Robin Hood",
                        "A fox who robs from the rich and gives to the poor",
                        "http://www.impawards.com/1973/posters/robin_hood_ver1_xlg.jpg",  # noqa
                        "https://www.youtube.com/watch?v=c5Qph47c2uE")

step_brothers = media.Movie("Step Brothers",
                     "Two step brothers, Jon Stamos, and a friendship",
                     "http://www.gstatic.com/tv/thumb/movieposters/175884/p175884_p_v8_ag.jpg",  # noqa
                     "https://www.youtube.com/watch?v=8QKE96wZTkw")

snatch = media.Movie("Snatch",
                     "A man and his caravan, with some dimonds and stuff",
                     "http://www.impawards.com/2000/posters/snatch_xlg.jpg",
                     "https://www.youtube.com/watch?v=9Jar2XkBboo")

the_devils_rejects = media.Movie("The Devils Rejects",
                                 "Sadistic family runs a rampage",
                                 "http://www.impawards.com/2005/posters/devils_rejects.jpg",  # noqa
                                 "https://www.youtube.com/watch?v=poDGH1_FzuY")

amelie = media.Movie("Amelie",
                     "A fantatic joureny with a girl and her imaginaton",
                     "https://images-na.ssl-images-amazon.com/images/I/51rE7KZvT2L._SY450_.jpg",  # noqa
                     "https://www.youtube.com/watch?v=2UT5xaAfxWU")

space_jam = media.Movie("Space Jam",
                        "Bugs and MJ take aliens in\
                        a high stakes game of B-ball",
                        "http://i.ebayimg.com/00/s/NTAwWDMzOA==/z/ne8AAMXQrhdTWH6R/$_3.JPG?set_id=2",  # noqa
                        "https://www.youtube.com/watch?v=IzU0x1tlfSQ")

goonies = media.Movie("Goonies",
                      "Some kids from the boondocks try\
                      to save thier neighborhood",
                      "https://images-na.ssl-images-amazon.com/images/I/61w2wGIKvqL.jpg",  # noqa
                      "https://www.youtube.com/watch?v=kFEfHCJG4G4")

he_man = media.Movie("Masters of the Universe",
                     "By the power of grey skull",
                     "http://www.impawards.com/1987/posters/masters_of_the_universe_xlg.jpg",  # noqa
                     "https://www.youtube.com/watch?v=CF20B8p4F08")

home_alone = media.Movie("Home Alone",
                      "A kid get left alone on Christmas",
                      "https://s-media-cache-ak0.pinimg.com/originals/00/a0/27/00a027ae2dd28fa6658a41e9c700d17e.jpg",  # noqa
                      "https://www.youtube.com/watch?v=IsOlj-xpK9Q")

# This array is where we can call the movies to be diplayed on the site.
# Order of name will effect the order they are displayed

movies = [robin_hood,
          step_brothers,
          snatch,
          the_devils_rejects,
          amelie, space_jam,
          goonies,
          he_man,
          home_alone]

fresh_tomatoes.open_movies_page(movies)
print(media.Movie.__doc__)
