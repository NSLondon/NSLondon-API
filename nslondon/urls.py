from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from nslondon.views import EventListView, EventDetailView


urlpatterns = patterns('',
    url(r'^events/$', EventListView.as_view(), name='event_list'),
    url(r'^events/(?P<pk>\d+)/$', EventDetailView.as_view(), name='event_detail'),

    # Examples:
    # url(r'^$', 'nslondon.views.home', name='home'),
    # url(r'^nslondon/', include('nslondon.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
