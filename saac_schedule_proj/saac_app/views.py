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
            "name": event.name,
            "desc": event.description,
            "date": event.date.isoformat(),
            "subc": event.subcommittee,
        })

    return JsonResponse(events_list, safe=False)
