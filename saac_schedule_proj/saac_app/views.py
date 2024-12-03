from .models import Event
from django.http import JsonResponse
from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm

def login(request):
    return render(request, 'registration/login.html')

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})
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
