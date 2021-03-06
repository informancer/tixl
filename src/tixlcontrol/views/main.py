from django.shortcuts import render
from django.views.generic import ListView

from tixlbase.models import Event


class EventList(ListView):
    model = Event
    context_object_name = 'events'
    template_name = 'tixlcontrol/events/index.html'

    def get_queryset(self):
        return Event.objects.filter(
            permitted__id__exact=self.request.user.pk
        ).prefetch_related(
            "organizer",
        )


def index(request):
    return render(request, 'tixlcontrol/base.html', {})
