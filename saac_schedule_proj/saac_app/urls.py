from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('calendar', views.calendar, name='calendar'),
    path('api/events', views.events_api, name='events_api'),
]
