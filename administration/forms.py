# users/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.db import models
from django.forms import ModelForm
from main.models import Club


class ClubCreationForm(ModelForm):
    class Meta:
        model = Club
        fields = ['club_name']