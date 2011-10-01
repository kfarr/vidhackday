from django.conf.urls.defaults import patterns, include, url
from django.views.generic.simple import direct_to_template

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'review.views.index_view'),
    url(r'^review/create/$', 'review.views.create_review'), # Create new review
    url(r'^review/(?P<review_id>\w+)/$', 'review.views.view_review', {}, ), # Show existing review

#    url(r'^splash/$', direct_to_template, {'template': 'index.html'}),
#    url(r'^dashboard/$', 'review.views.dashboard_view'), # Displays list of both currencies/holdings, transactions, and button to add new currency
#    url(r'^about/$', direct_to_template, {'template': 'about.html'}),
#    url(r'^faq/$', direct_to_template, {'template': 'faq.html'}),
#    url(r'^accounts/', include('registration.backends.simple.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
