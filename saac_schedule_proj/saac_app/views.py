from django.shortcuts import render
from .models import Event
from django.http import JsonResponse

def home(request):
    events = Event.objects.all()
    return render(request, 'home.html', {'events': events})

def calendar(request):
    events = Event.objects.all()
    return render(request, 'calendar.html', {'events': events})

def events_api(request):
    events = Event.objects.all()
    events_list = []

    for event in events:
        events_list.append({
            "title": event.title,
            "desc": event.description,
            "start": event.start.isoformat(),
            "end": event.end.isoformat(),
            "loc": event.location,
            "subc": event.subcommittee,
        })

    return JsonResponse(events_list, safe=False)
