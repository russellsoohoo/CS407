from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['sport'].widget = forms.Select(choices=CustomUser.SPORTS)
        for field_name, field in self.fields.items():
            field.required = True

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['email',
                  'first_name',
                  'last_name',
                  'sport',
                  'grad_year',
                  ]

class PasswordChangeForm(forms.Form):
    old_password = forms.CharField(widget=forms.PasswordInput, label="Old Password")
    new_password1 = forms.CharField(widget=forms.PasswordInput, label="New Password")
    new_password2 = forms.CharField(widget=forms.PasswordInput, label="Confirm New Password")