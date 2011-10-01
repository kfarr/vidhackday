from review.models import Review, UserProfile
from django.contrib import admin

#class CurrencyAdmin(admin.ModelAdmin):
#	filter_horizontal = ('users_can_receive',)

admin.site.register(Review)
admin.site.register(UserProfile)
