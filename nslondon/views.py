from django.views.generic import DetailView

from nslondon.models import Event


class EventDetailView(DetailView):
    model = Event

