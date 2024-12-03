from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    sport = forms.CharField()

    class Meta:
        model = CustomUser
        fields = ['email',
                  'password1',
                  'password2',
                  'first_name',
                  'last_name',
                  'sport',
                  'grad_year',
                  ]

    email = forms.EmailField(required=True)
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    sport = forms.CharField(required=True)
    grad_year = forms.IntegerField(required=True)
