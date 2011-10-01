from django.conf.urls.defaults import patterns, include, url
from django.views.generic.simple import direct_to_template

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'currency.views.index_view'),

    url(r'^splash/$', direct_to_template, {'template': 'index.html'}),

    url(r'^dashboard/$', 'currency.views.dashboard_view'), # Displays list of both currencies/holdings, transactions, and button to add new currency

    url(r'^currency/(?P<short_symbol>\w+)/$', 'currency.views.currency_view', {}, ), # Show existing currency
    url(r'^currency/$', 'currency.views.currency_view'), # Create new currency

    url(r'^transaction/$', 'currency.views.transaction_view'), # Create new transaction
    url(r'^transaction/(?P<transaction_id>\w+)/$', 'currency.views.transaction_view'), # DON'T NEED THIS

    url(r'^about/$', direct_to_template, {'template': 'about.html'}),
    url(r'^faq/$', direct_to_template, {'template': 'faq.html'}),

    url(r'^accounts/', include('registration.backends.simple.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
