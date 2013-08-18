from django.db import models
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

    def __unicode__(self):
        return self.name


class Event(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    venue = models.ForeignKey(Venue)
    organiser = models.ForeignKey(User, related_name='events')

    start_time = models.DateTimeField()
    end_time = models.DateTimeField()


class Talk(models.Model):
    event = models.ForeignKey(Event)
    speaker = models.ForeignKey(User, related_name='speakers')

