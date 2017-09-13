#class
import webbrowser

class Movie():
	VALID_RATINGS = ["G", "PG", "PG-13", "R"]
	def __init__(self, movie_title, movie_storyline, poster_image, tailer_youtube):
		self.title = movie_title
		self.storyline = movie_storyline
		self.poster_image_url = poster_image
		self.trailer_youtube_url = tailer_youtube

	#rating method to define movie raings
	def set_ratings(self, rating):
		self.rating = rating if rating in self.VALID_RATINGS else 'Not available'