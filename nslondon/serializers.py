from rest_framework import serializers

from nslondon.models import Venue, Event, Talk

class VenueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Venue


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event


class TalkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Talk

