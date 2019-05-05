from django.conf import settings
from django.contrib.auth.models import User
from django.db import models

# Create your models here.


# messages
class Message(models.Model):
    message_header = models.CharField(max_length=100)
    message_body = models.CharField(max_length=400)
    date_time = models.DateTimeField()
    # specify foreign key on author of message
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)  # Default model for Users
    # on_delete=models.PROTECT - Forbid the deletion of the referenced object.
    # To delete it you will have to delete all objects that reference it manually.
    # SQL equivalent: RESTRICT.


class Club (models.Model):
    club_id = models.IntegerField(primary_key=True)
    club_name = models.CharField(max_length=30)


class Portfolio (models.Model):
    portfolio_id = models.IntegerField(primary_key=True)
    portfolio_name = models.CharField(max_length=30)


class StudentClubRelation(models.Model):
    user_id = models.CharField(max_length=10)
    club_id = models.ForeignKey(Club, on_delete=models.CASCADE)
    portfolio_id = models.ForeignKey(Portfolio, on_delete=models.CASCADE)


class WitsSportExecutive(models.Model):
    user_id = models.CharField(max_length=10)
    portfolio_id = models.ForeignKey(Portfolio, on_delete=models.CASCADE)


class WitsSport(models.Model):
    user_id = models.CharField(max_length=10)
    portfolio_id = models.ForeignKey(Portfolio, on_delete=models.CASCADE)


class UserDetails(models.Model):
    user_id = models.CharField(max_length=10)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email_address = models.CharField(max_length=30)
    contact_number = models.IntegerField()