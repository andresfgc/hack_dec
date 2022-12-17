from django.shortcuts import render


def event(request):
    return render(request, 'events/event.html')


def events_list(request):
    return render(request, 'events/events-list.html')


def add_event(request):
    return render(request, 'events/add-event.html')
