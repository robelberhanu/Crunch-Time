# users/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.core.exceptions import ValidationError
from django.db import models
from django.forms import ModelForm
from django.shortcuts import get_object_or_404

from main.models import Club, StudentClubRelation, Portfolio
from users.models import CustomUser


class ClubCreationForm(ModelForm):
    class Meta:
        model = Club
        portfolio = models.ForeignKey(Portfolio, null=True, blank=True, on_delete=models.CASCADE)
        fields = ['club_name']


class StudentClubRelationCreationForm(ModelForm):
    class Meta:
        model = StudentClubRelation
        fields = ['user_id','portfolio_id']
        unique_together = ('user_id','portfolio_id')
        # club_id = ""

    def __init__(self, *args, **kwargs):
        self.club_id = kwargs.pop('club_id', None)
        super().__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = self.cleaned_data

        user_field = cleaned_data.get('user_id')
        portfolio_field = cleaned_data.get('portfolio_id')
        # club_field = cleaned_data.get('club_id')

        student_club_objects = StudentClubRelation.objects.filter(user_id=user_field, club_id=self.club_id)
        student_club_portfolios = StudentClubRelation.objects.filter(club_id = self.club_id, portfolio_id=portfolio_field)

        is_exec = False
        portfolio_execs = StudentClubRelation.objects.filter(club_id = self.club_id, portfolio_id__portfolio_name=portfolio_field, portfolio_id__is_Exec= True)

        if len(portfolio_execs)>0:
            is_exec = True

        if len(student_club_portfolios) > 0 & is_exec:
            msg = "Multiple user with same exec position is not allowed"
            self._errors["portfolio_id"] = self.error_class([msg])
            del cleaned_data["portfolio_id"]
            raise ValidationError(msg)

        if len(student_club_objects) > 0:
            msg = u"This user is already part of this club"
            self._errors["user_id"] = self.error_class([msg])
            del cleaned_data["user_id"]
            raise ValidationError(msg)

        return cleaned_data
        # objects = StudentClubRelation.objects.filter()


class EditUserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'first_name', 'last_name', 'email', 'contact_number', 'id_number']

# def delete_club_member(request,*pks):
#     for pk in pks:
#         m = StudentClubRelation.objects.get(pk=id)
#         m.delete()
#
#
# def delete_club_member(request,*pks):
#     for pk in pks:
#         m = Club.objects.get(pk=id)
#         m.delete()
#
#
# def delete_user(request,*pks):
#     for pk in pks:
#         m = CustomUser.objects.get(pk=id)
#         m.delete()