from django.db import models
from django.utils import timezone


class Event(models.Model):
    SUBCOMMITTEES = {
        "BeOregon": "BeOregon",
        "Athlete Unification": "Athlete Unification",
        "Duck The Stigma": "Duck The Stigma",
        "O Heroes": "OHeroes",
        "Women Of Oregon": "Women Of Oregon",
        "SAAC": "SAAC",
        "Ducks Go Pro": "Ducks Go Pro",
    }
    title = models.CharField(max_length=100)  # name of event
    description = models.TextField()  # description of event
    start = models.DateTimeField(default=timezone.now)  # start date of event
    end = models.DateTimeField(default=timezone.now)  # end date of event
    location = models.CharField(max_length=100, default="TBD")  # location of event
    subcommittee = models.CharField(max_length=20, choices=SUBCOMMITTEES)  # subcommittee of event

    def __str__(self):
        return self.title
