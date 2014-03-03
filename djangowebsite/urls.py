from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin

admin.autodiscover()

import hurricanes.views

# http://127.0.0.1:8000/map/
urlpatterns = patterns('',
                       url('^map/$', hurricanes.views.earthquake))


