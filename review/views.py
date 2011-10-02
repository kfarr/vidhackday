from review.models import Review, UserProfile
from movie.models import Movie

from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt

def index_view(request):
#	if request.user.is_authenticated():
#		return dashboard_view(request)
	return render_to_response('index.html', {}, context_instance=RequestContext(request))

def dashboard_view(request):
	reviews = Review.objects.filter(user=request.user)
	return render_to_response('dashboard.html', {'reviews':reviews}, context_instance=RequestContext(request))

def view_review(request, review_id = None):
	review = get_object_or_404(Review, id = review_id)
	return render_to_response('view_review.html', {'review': review}, context_instance=RequestContext(request))

@login_required
def create_review(request):
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

	movies = Movie.objects.all()
	return render_to_response('create_review.html', {'form': form, 'movies': movies}, context_instance=RequestContext(request))


@csrf_exempt
@login_required
def save_archive_ajax(request):
    if request.is_ajax():
	# Goal is to save archive_id witha new object with teh new dude and movie id

	movie_id = request.POST['movie_id'] 
	archive_id = request.POST['archive_id']
	
	messages.success(request, "This review has been saved. %s %s" % movie_id, archive_id)

        data = json.dumps({'state': state, 'message': msg, 'shortname': dest.short_name})
        return HttpResponse(data, 'application/javascript')
    else:
	msg = "Error"
        return HttpResponse(msg)


