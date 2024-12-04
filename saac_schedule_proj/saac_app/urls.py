from django.urls import path, include
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.calendar, name='home'),
    path('calendar/', views.calendar, name='calendar'),
    path('calendar/api/events/', views.events_api, name='events_api'),
    path('profile/', views.profile, name='profile'),
    path('login/', views.login, name='login'),  # change to and import LoginView?
    path('logout/', LogoutView.as_view(next_page='/login/'), name='logout'),
    path('signup/', views.signup, name='signup'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('events/<int:event_id>/register/', views.register_for_event, name='register_for_event'),
    path('events/<int:event_id>/unregister/', views.unregister_for_event, name='unregister_from_event'),
]
