from .models import Event
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  # Replace 'home' with your desired URL
        else:
            form = AuthenticationForm()
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')

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
