from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	(r'^$', 'mlb.views.index'),
    (r'^nba/$', 'nba.views.index'),
	(r'^mlb/$', 'mlb.views.index'),
	(r'^mlb/player/(?P<playerID>[a-z]+\d{2})/$', 'mlb.views.player'),
	
	(r'^mlb/leaderApi/(?P<fieldAbbrev>[A-Za-z]+)/$', 'mlb.views.leaderApi'),
	(r'^mlb/leaderTableApi/(?P<fieldAbbrev>[A-Za-z]+)/$', 'mlb.views.leaderTableApi'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),

	#(r'^site_media/(?P<path>.*)$', 'django.views.static.serve',
	#      {'document_root': '/Users/danieldelany/Documents/Sports Stats/django/sportsstats/media', 'show_indexes':True})
			
)
