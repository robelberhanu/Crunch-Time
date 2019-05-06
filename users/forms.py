# users/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('username',)

    # # A password is not required to create user - Other authentication will be used
    # def __init__(self, *args, **kargs):
    #     super(CustomUserCreationForm, self).__init__(*args, **kargs)
    #     self.fields['password1'].required = False
    #     self.fields['password2'].required = False
    #     self.fields.pop('password1')
    #     self.fields.pop('password2')


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'email')