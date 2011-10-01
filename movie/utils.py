from movie.models import Movie

def sync_RT_movies(list = 'box_office'):
	# Lists could be: box_office, in_theaters, opening, and upcoming
	from rottentomatoes import RT
	rt = RT()

	movies = rt.movies(list)

	for movie in movies:
		movie_obj, created = Movie.objects.get_or_create(RT_movie_id = movie['id'])
		movie_obj.title = movie['title']
		movie_obj.poster_detailed = movie['posters']['detailed']
		movie_obj.save()
		print movie_obj
		print "********"
