from django.db import models
from users.models import CustomUser

# Create your models here.


class Club (models.Model):
    club_id = models.IntegerField(primary_key=True)
    club_name = models.CharField(max_length=30)


class Portfolio (models.Model):
    portfolio_id = models.IntegerField(primary_key=True)
    portfolio_name = models.CharField(max_length=30)

    def __str__(self):
        return self.portfolio_name


class StudentClubRelation(models.Model):
    # user_id = models.CharField(max_length=10)
    user_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE, unique=True)
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