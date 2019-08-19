from django.db import models

# Create your models here.
# Should move this into specific class
import users.models


class Club(models.Model):
    name = models.CharField(max_length=30)
    # members = models.ManyToManyField(users.models.CustomUser, through='Membership') # Not required for now

    def __str__(self):
        return self.name


class Position(models.Model):
    name = models.CharField(max_length=30)
    isExec = models.BooleanField()

    def __str__(self):
        return self.name


class Membership(models.Model):  # Works as relational table between club and user
    club = models.ForeignKey(Club, on_delete=models.CASCADE)
    user = models.ForeignKey(users.models.CustomUser, on_delete=models.CASCADE)
    position = models.ForeignKey(Position, on_delete=models.CASCADE)

    def __str__(self):
        return self.club.name + "-" + self.user.username + "-" + self.position.name

    class Meta:
        unique_together = ('club', 'user',)
