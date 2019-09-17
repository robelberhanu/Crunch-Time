from django.db import models
from users.models import CustomUser

# Create your models here.


class Club (models.Model):
    club_id = models.IntegerField(primary_key=True)
    club_name = models.CharField(max_length=30)
    is_deleted = models.BooleanField()


class Portfolio (models.Model):
    portfolio_id = models.IntegerField(primary_key=True)
    portfolio_name = models.CharField(max_length=30)
    is_Exec = models.BooleanField()

    def __str__(self):
        return self.portfolio_name


class StudentClubRelation(models.Model):
    # user_id = models.CharField(max_length=10)
    user_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    club_id = models.ForeignKey(Club, on_delete=models.CASCADE)
    portfolio_id = models.ForeignKey(Portfolio, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('club_id', 'user_id',)  # Table cannot have multiple rows that share the same club_id and user_id combination

    def __str__(self):
        return self.user_id.username + "," + self.club_id.club_name + "," + self.portfolio_id.portfolio_name


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