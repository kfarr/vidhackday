from django.forms import ModelForm

from review.models import Review
from django.contrib.admin import widgets                                       
from django.forms import ModelForm, Textarea

class ReviewForm(ModelForm):
	class Meta:
		model = Review
#		exclude = ('owner','users_can_receive','allow_free_trade',)
		
