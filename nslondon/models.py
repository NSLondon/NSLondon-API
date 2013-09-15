from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic
from django.contrib.auth.models import User


class Venue(models.Model):
    name = models.CharField(max_length=255)

    longitude = models.FloatField()
    latitude = models.FloatField()

    # Address
    address_1 = models.CharField(max_length=255)
    address_2 = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=255)
    county = models.CharField(max_length=255, blank=True, null=True)
    post_code = models.CharField(max_length=255)
    country = models.CharField(max_length=255, blank=True, null=True)

    notes = models.TextField(blank=True, null=True)

    def __unicode__(self):
        return self.name

    @property
    def address(self):
        lines = (self.address_1, self.address_2, self.city, self.county, self.post_code, self.country)

        lines = [line for line in lines if line]

        return ', '.join(lines)


class Event(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    venue = models.ForeignKey(Venue)
    organiser = models.ForeignKey(User, related_name='events')

    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    def __unicode__(self):
        return self.name

    @models.permalink
    def get_absolute_url(self):
        return ('event_detail', (), { 'pk': self.pk })



class Talk(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    event = models.ForeignKey(Event, related_name='talks')
    speaker = models.ForeignKey(User, related_name='speakers')

    links = generic.GenericRelation('Link')

    def __unicode__(self):
        return self.name

class Link(models.Model):
    name = models.CharField(max_length=255)
    url = models.URLField()
    is_embed = models.BooleanField(default=True)

    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = generic.GenericForeignKey('content_type', 'object_id')

    def __unicode__(self):
        return self.url
