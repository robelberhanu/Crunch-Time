from django.db import models

# Create your models here.
# Should move this into specific class
import users.models


class Club(models.Model):
    name = models.CharField(max_length=30)
    members = models.ManyToManyField(users.models.CustomUser, through='Membership')


class Portfolio(models.Model):
    name = models.CharField(max_length=30)
    isExec = models.BooleanField()

    def __str__(self):
        return self.name


class Membership(models.Model):  # Works as relational table between club and user
    club = models.ForeignKey(Club, on_delete=models.CASCADE)
    user = models.ForeignKey(users.models.CustomUser, on_delete=models.CASCADE)
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE)
