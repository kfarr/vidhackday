from django.core.management.base import BaseCommand, CommandError
import datetime

class Command(BaseCommand):
	help = 'Sync top box office movies from Rotten Tomatoes'

	def handle(self, *args, **options):
		try:
			from movie.utils import sync_RT_movies
			sync_RT_movies()
		except:
			import traceback
			print '[%s] Error: %s' % (datetime.datetime.now(), traceback.format_exc())
