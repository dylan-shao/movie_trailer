#class
import webbrowser
import media

class Movie(media.Media):
	#like static variable which is class level
	VALID_RATINGS = ["G", "PG", "PG-13", "R"]
	def __init__(self, movie_title, movie_storyline, poster_image, tailer_youtube, rating):
		#inheritance, title is from parent media
		media.Media.__init__(self, movie_title)
		self.storyline = movie_storyline
		self.poster_image_url = poster_image
		self.trailer_youtube_url = tailer_youtube
		self.rating = rating if rating in self.VALID_RATINGS else 'N/A'