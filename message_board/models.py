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

