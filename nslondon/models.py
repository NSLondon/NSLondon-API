from django.db import models


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

