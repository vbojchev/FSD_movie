# I'm reusing existing code from fresh_tomatoes and our class declaration is in media
import media
import fresh_tomatoes

# every movie has (Title, Storyline, poster_url, youtube_trailer_url)
toy_story = media.Movie("Toy Story 1", "Toys can be mean to each other",
                        "http://cdn.movieweb.com/img.site/PHcZdLV7C3qNgc_1_l.jpg",
                        "https://www.youtube.com/watch?v=4KPTXpQehio")
avatar = media.Movie("Avatar", "A guy gets very into the movie",
                        "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRMYL7QMFtZXlUqq_T1p8kU26slKZeexCnAaNcuuGVnSoUYjVEMGRjihA",
                        "https://www.youtube.com/watch?v=5PSNL1qE6VY")
beaking_bread = media.Movie("Baking Bread", "Two guys cook",
                            "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRP9VNRpxCWvoj4wAdUpNvcU35khZEUkszp5GQogMJ-hmgLU71v1Q",
                            "https://www.youtube.com/watch?v=5hygpAubW2E")
princess_mononoke = media.Movie("Princess Mononoke", "Japaneese prince cuts his hair and goes to save the world",
                        "http://t2.gstatic.com/images?q=tbn:ANd9GcS3ReuE3ksrdNabf0K7frhelHm-05ec4a_1mIxQUqNiRduHNrJ5",
                        "https://https://www.youtube.com/watch?v=4OiMOHRDs14")
panda = media.Movie("Kung Fu Panda", "Special ingrediant is love, then you kick ass",
                        "http://www.gstatic.com/tv/thumb/movieposters/175618/p175618_p_v8_ad.jpg",
                        "https://www.youtube.com/watch?v=PXi3Mv6KMzY")


# fresh tomatoes's open_movies_page function accepts list of movies
movies = [toy_story, avatar, beaking_bread, princess_mononoke, panda]

#print(media.Movie.__doc__)
#print(media.Movie.__name__)
#print(media.Movie.__module__)

fresh_tomatoes.open_movies_page(movies)
