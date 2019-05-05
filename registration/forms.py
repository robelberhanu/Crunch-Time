from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


# alter Register Form

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username',)

# class CustomUserCreationForm(forms.Form):

