from django.shortcuts import render
from events.models import Event


def event(request):
    return render(request, 'events/event.html')


def events_list(request, event_type_arg):
    if event_type_arg == 'all':
        events = Event.objects.all()
        event_type = 'All Events'
    else:
        events = Event.objects.all()

    context = {
        'events': events,
        'event_type': event_type
    }

    return render(request, 'events/events-list.html', context)


def add_event(request):
    return render(request, 'events/add-event.html')


def edit_event(request):
    return render(request, 'events/edit-event.html')
