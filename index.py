import fresh_tomatoes
import movie

toy_story = movie.Movie("Toy Stroy", 
						"A story of a boy and his toys that come to life", 
						"https://lumiere-a.akamaihd.net/v1/images/open-uri20150422-12561-a29xp6_8e57696e.jpeg", 
						"https://www.youtube.com/watch?v=KYz2wyBy3kc")

avatar2 = movie.Movie("Avatar 2", 
					"A story about avatar, 2nd movie",
					"https://i.ytimg.com/vi/Bl8fkc4HsSs/maxresdefault.jpg",
					"https://www.youtube.com/watch?v=RqHI0kE-cyo")

moana = movie.Movie("Moana", 
					"A story about moana",
					"https://t3.gstatic.com/images?q=tbn:ANd9GcTJOaSVrzlgewVqmUgUz4W5ty2KUeHH6s-aYSIr_Qw8v2EBrtCS",
					"https://www.youtube.com/watch?v=LKFuXETZUsI")

toy_story.set_ratings("G")
avatar2.set_ratings("f")
moana.set_ratings("G")
movies = [toy_story, avatar2, moana]
fresh_tomatoes.open_movies_page(movies)

