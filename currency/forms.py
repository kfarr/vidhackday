from django.forms import ModelForm

from currency.models import Currency, Transaction
from django.contrib.admin import widgets                                       
from django.forms import ModelForm, Textarea

class CurrencyForm(ModelForm):
	class Meta:
		model = Currency
		exclude = ('owner','users_can_receive','allow_free_trade',)
		
class TransactionForm(ModelForm):
	class Meta:
		model = Transaction
