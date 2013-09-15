from rest_framework import serializers

from django.contrib.auth.models import User
from nslondon.models import Venue, Event, Talk, Link

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name')


class LinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Link
        fields = ('name', 'url', 'is_embed')


class VenueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Venue


class TalkSerializer(serializers.ModelSerializer):
    speaker = UserSerializer()
    links = LinkSerializer()

    class Meta:
        model = Talk

class EventSerializer(serializers.ModelSerializer):
    venue = VenueSerializer()
    talks = TalkSerializer()
    organiser = UserSerializer()
    url = serializers.CharField(source='get_absolute_url', read_only=True)

    class Meta:
        model = Event
        fields = ('id', 'url', 'name', 'description', 'organiser', 'venue', 'start_time', 'end_time', 'talks')
