from review.models import Review
from movie.models import Movie

from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required

def view_movie(request, RT_movie_id = None):
	movie = get_object_or_404(Movie, RT_movie_id = RT_movie_id)
	reviews = Review.objects.get(movie = movie)
	return render_to_response('view_movie.html', {'movie': movie, 'reviews': review}, context_instance=RequestContext(request))


