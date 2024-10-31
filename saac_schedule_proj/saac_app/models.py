from django.db import models
from django.utils import timezone


class Event(models.Model):
    SUBCOMMITTEES = {
        "bo": "BeOregon",
        "au": "Athlete Unification",
        "dts": "Duck The Stigma",
        "oh": "OHeroes",
        "woo": "Women Of Oregon",
        "s": "SAAC",
        "dgp": "Ducks Go Pro",
    }
    title = models.CharField(max_length=100) # name of event
    description = models.TextField() # description of event
    start = models.DateTimeField(default=timezone.now)  # start date of event
    end = models.DateTimeField(default=timezone.now) # end date of event
    location = models.CharField(max_length=100, default="TBD") # location of event
    subcommittee = models.CharField(max_length=3, choices=SUBCOMMITTEES) # subcommittee of event

    def __str__(self):
        return self.title
