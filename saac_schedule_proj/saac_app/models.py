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
    name = models.CharField(max_length=100) # name of event
    description = models.TextField() # description of event
    date = models.DateTimeField()  # date of event
    subcommittee = models.CharField(max_length=3, choices=SUBCOMMITTEES) # subcommittee of event

    def __str__(self):
        return self.name
