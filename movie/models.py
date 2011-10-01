from django.db import models

class Movie(models.Model):
	RT_movie_id = models.CharField(max_length=50) # Movie ID in Rotten Tomatoes
	title = models.CharField(max_length=255)
	poster_detailed = models.URLField()
	created_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.title
