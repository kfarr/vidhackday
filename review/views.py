from review.models import Review, UserProfile

from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required

def index_view(request):
#	if request.user.is_authenticated():
#		return dashboard_view(request)
	return render_to_response('index.html', {}, context_instance=RequestContext(request))

@login_required
def create_review_view(request):
	# Create one review
	from review.forms import ReviewForm

	if request.method == 'POST':
		form = ReviewForm(request.POST)
#		if review: form = ReviewForm(request.POST, instance=review)

		if form.is_valid():
			instance = form.save()
			messages.success(request, "This review has been saved.")
			instance.user = request.user
			instance.save()
#			return HttpResponseRedirect(reverse('review.views.dashboard_view', ))
		else:
			messages.error(request, "Unable to save this review.")
	else:
		form = ReviewForm()
#		if review: form = ReviewForm(instance = review)

	return render_to_response('create_review.html', {'form': form}, context_instance=RequestContext(request))

