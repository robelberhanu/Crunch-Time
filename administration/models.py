from django.db import models

# Create your models here.
# Should move this into specific class
import users.models


class Club(models.Model):
    name = models.CharField(max_length=200)