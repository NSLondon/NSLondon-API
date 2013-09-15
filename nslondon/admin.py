from django.contrib import admin
from nslondon.models import Venue, Event, Talk, Link

class VenueAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('name',),
        }),
        ('Location', {
            'fields': ('longitude', 'latitude',),
        }),
        ('Address', {
            'fields': ('address_1', 'address_2', 'city', 'county', 'post_code', 'country')
        }),
    )

class EventAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('name', 'description')
        }),
        (None, {
            'fields': ('venue', 'organiser'),
        }),
        (None, {
            'fields': ('start_time', 'end_time'),
        }),
    )

class TalkAdmin(admin.ModelAdmin):
    pass

class LinkAdmin(admin.ModelAdmin):
    pass

admin.site.register(Venue, VenueAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(Talk, TalkAdmin)
admin.site.register(Link, LinkAdmin)

