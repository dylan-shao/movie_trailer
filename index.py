import fresh_tomatoes
import movie
import json

def create_instance(m):
	return movie.Movie(m["movie_title"], m["movie_storyline"], m["poster_image"], m["trailer_youtube_url"], m["rating"])

with open('movies.json') as movies_data:
    movies_data = json.load(movies_data)

movies_list = []
for m in movies_data:
	movies_list.append(create_instance(m))

fresh_tomatoes.open_movies_page(movies_list)

