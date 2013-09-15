from rest_framework import generics
from rest_framework import mixins

from nslondon.models import Event
from nslondon.serializers import EventSerializer


class EventListView(mixins.ListModelMixin, generics.GenericAPIView):
    model = Event
    serializer_class = EventSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class EventDetailView(mixins.RetrieveModelMixin, generics.GenericAPIView):
    model = Event
    serializer_class = EventSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


