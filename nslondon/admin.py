from django.contrib import admin
from nslondon.models import Venue, Event, Talk

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

admin.site.register(Venue, VenueAdmin)

