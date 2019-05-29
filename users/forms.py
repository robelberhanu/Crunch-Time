# users/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('username', 'first_name', 'last_name', 'email', 'contact_number', 'id_number') # , 'first_name', 'last_name', 'email', 'contact_number'

    # A password is not required to create user - Other authentication will be used
    def __init__(self, *args, **kargs):
        super(CustomUserCreationForm, self).__init__(*args, **kargs)
        self.fields['password1'].required = False
        self.fields['password2'].required = False
        self.fields['id_number'].required = True
        # self.fields['contact_number'].required = False
        # self.fields.pop('password1')
        # self.fields.pop('password2')

    # def save(self, commit=True):
    #     user = super(CustomUserCreationForm, self).save(commit=False)
    #     # first_name, last_name = self.cleaned_data["fullname"].split()
    #     user.first_name = self.cleaned_data['first_name']
    #     user.last_name = self.cleaned_data['last_name']
    #     user.email = self.cleaned_data["email"]
    #     user.contact_number = self.cleaned_data["contact_number"]
    #     return user


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'email')