from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import MinValueValidator


# add extra attributes to user model here
class CustomUser(AbstractUser):
    contact_number = models.IntegerField(null=True)
    id_number = models.IntegerField(null=False, validators=[MinValueValidator(100000)])

