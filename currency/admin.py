from currency.models import Currency, Transaction, UserProfile, Holding
from django.contrib import admin

class CurrencyAdmin(admin.ModelAdmin):
	filter_horizontal = ('users_can_receive',)

admin.site.register(Currency, CurrencyAdmin)
admin.site.register(Transaction)
admin.site.register(UserProfile)
admin.site.register(Holding)
