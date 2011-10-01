from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Transaction States
DENIED = -1
REQUESTED = 0
APPROVED = 1

TRANSACTION_STATES = (
        (DENIED, 'Denied'),
        (REQUESTED, 'Requested'),
        (APPROVED, 'Approved'),
)

class Currency(models.Model):
	long_name = models.CharField(max_length=100)
	short_symbol = models.CharField(max_length=10, unique=True) # ABEOF
	total_units = models.IntegerField() # Total number of currency units in ecosystem
	created = models.DateTimeField(auto_now_add=True)
	owner = models.ForeignKey(User, related_name='owner', blank=True, null=True)
	expiration_date = models.DateField(blank=True, null=True)
	allow_free_trade = models.BooleanField(default=True)
	users_can_receive = models.ManyToManyField(User, related_name='recipients',blank=True, null=True)

	class Meta:
		verbose_name_plural = "currencies"

	def __str__(self):
		return "%s (%s)" % (self.long_name, self.short_symbol)

class Transaction(models.Model):
	from_user = models.ForeignKey(User, related_name='from_user')
	from_currency = models.ForeignKey(Currency, related_name='from_currency', blank=True, null=True)
	from_item = models.CharField(max_length=60, blank=True)
	from_quantity = models.IntegerField(blank=True, null=True)

	to_user = models.CharField(max_length=60, blank=True)
	to_currency = models.ForeignKey(Currency, related_name='to_currency', blank=True, null=True)
	to_item = models.CharField(max_length=60, blank=True)
	to_quantity = models.IntegerField(blank=True, null=True)

	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	status = models.IntegerField(choices=TRANSACTION_STATES, default=REQUESTED)

	def __str__(self):
		return "Transaction by %s on %s" % (self.from_user.username, self.created_at)

class UserProfile(models.Model):
	user = models.OneToOneField(User)
	currencies = models.ManyToManyField(Currency, through='Holding')	# One holding for each user/currency relationship

	def __str__(self):
		return "%s UserProfile Obj" % (self.user.username)

def create_user_profile(sender, instance, created, **kwargs):  
	if created:  
		profile, created = UserProfile.objects.get_or_create(user=instance)  
post_save.connect(create_user_profile, sender=User) 

class Holding(models.Model):
	userprofile = models.ForeignKey(UserProfile)
	currency = models.ForeignKey(Currency)
	value = models.IntegerField()

	def __str__(self):
		return "%s holds %s of %s" % (self.userprofile.user.username, self.value, self.currency.short_symbol)

