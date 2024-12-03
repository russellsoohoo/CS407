from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser, BaseUserManager


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


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(email, password, **extra_fields)

class CustomUser(AbstractUser):
    username = None  # remove username field
    email = models.EmailField(unique=True)  # use email as username

    first_name = models.CharField(max_length=30)  # first name
    last_name = models.CharField(max_length=30)  # last name
    sport = models.CharField(max_length=20)  # sport
    grad_year = models.PositiveIntegerField(default=0000)  # graduation year

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'sport', 'grad_year']

    objects = CustomUserManager()

    def __str__(self):
        return self.email
