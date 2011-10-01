from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from movie.models import Movie

class Review(models.Model):
	title = models.CharField(max_length=100)
	user = models.ForeignKey(User, blank=True, null=True)
	archive_id = models.CharField(max_length=50, blank=True, null=True) # archive_id from TokBox
	movie = models.ForeignKey(Movie, blank=True, null=True)
	created_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return "Review by %s on ..." % (self.user.username)

class UserProfile(models.Model):
	user = models.OneToOneField(User)

	def __str__(self):
		return "%s UserProfile Obj" % (self.user.username)

def create_user_profile(sender, instance, created, **kwargs):  
	if created:  
		profile, created = UserProfile.objects.get_or_create(user=instance)  
post_save.connect(create_user_profile, sender=User) 

