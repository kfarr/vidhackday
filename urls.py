from django.conf.urls.defaults import patterns, include, url
from django.views.generic.simple import direct_to_template

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'review.views.index_view'),
    url(r'^review/create/$', 'review.views.create_review'), # Create new review
    url(r'^saveArchive/', 'review.views.save_archive_ajax'), # Save new archive_id from tokbox
    url(r'^review/(?P<review_id>\w+)/$', 'review.views.display_review', {}, ), # Show existing review
    url(r'^accounts/', include('registration.backends.simple.urls')),

    url(r'^dashboard/$', 'review.views.dashboard_view'), # Displays list of both currencies/holdings, transactions, and button to add new currency

    url(r'^movie/(?P<RT_movie_id>\w+)/$', 'movie.views.view_movie', {}, ), # Show reviews for movie

#    url(r'^splash/$', direct_to_template, {'template': 'index.html'}),
#    url(r'^about/$', direct_to_template, {'template': 'about.html'}),
#    url(r'^faq/$', direct_to_template, {'template': 'faq.html'}),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
