from django.contrib.auth.decorators import login_required
from .models import Event
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from .forms import CustomUserCreationForm, UserUpdateForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages

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

@login_required
def profile(request):
    user = request.user
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=user)
        password_form = PasswordChangeForm(request.POST)

        if 'update_info' in request.POST and user_form.is_valid():
            user_form.save()
            messages.success(request, 'Your profile has been updated.')
            return redirect('profile')

        if 'change_password' in request.POST and password_form.is_valid():
            old_password = password_form.cleaned_data['old_password']
            new_password1 = password_form.cleaned_data['new_password1']
            new_password2 = password_form.cleaned_data['new_password2']

            if not user.check_password(old_password):
                messages.error(request, 'Old password is incorrect.')
            elif new_password1 != new_password2:
                messages.error(request, 'New passwords do not match.')
            else:
                user.set_password(new_password1)
                user.save()
                update_session_auth_hash(request, user)  # Keep user logged in after password change
                messages.success(request, 'Your password has been changed.')
                return redirect('profile')
    else:
        user_form = UserUpdateForm(instance=user)
        password_form = PasswordChangeForm()

    context = {
        'user_form': user_form,
        'password_form': password_form,
    }
    return render(request, 'profile.html', context)

@login_required()
def calendar(request):
    events = Event.objects.all()
    return render(request, 'calendar.html', {'events': events})

@login_required()
def events_api(request):
    events = Event.objects.all()
    events_list = []

    for event in events:
        events_list.append({
            "id": event.id,  # Add event ID
            "title": event.title,
            "desc": event.description,
            "start": event.start.isoformat(),
            "end": event.end.isoformat(),
            "loc": event.location,
            "subc": event.subcommittee,
            # "registered_users": event.registered_users
        })

    return JsonResponse(events_list, safe=False)

@login_required
def register_for_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)

    if request.user in event.registered_users.all():
        messages.warning(request, "You are already registered for this event.")
    else:
        event.registered_users.add(request.user)
        messages.success(request, f"You have successfully registered for {event.name}.")

    return redirect('event_detail', event_id=event.id)
