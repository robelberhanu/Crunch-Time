from django.contrib.auth.models import AbstractUser
from django.db import models


# add extra attributes to user model here
class CustomUser(AbstractUser):
    contact_number = models.IntegerField(null=True)
