from django.conf import settings
# from django.contrib.auth.models import User
from django.db import models

import users.models

# Create your models here.

# class MessageBoard(models.Model):
#     messageboard_id = models.IntegerField(primary_key=True)
#     messageboard_name = models.CharField(max_length=100)

# messages
class Message(models.Model):
    message_header = models.CharField(max_length=100)
    message_body = models.CharField(max_length=400)
    date_time = models.DateTimeField()
    message_board_name = models.CharField(max_length=100)
    # specify foreign key on author of message
    user = models.ForeignKey(users.models.CustomUser, on_delete=models.PROTECT)  # Default model for Users

    # on_delete=models.PROTECT - Forbid the deletion of the referenced object.
    # To delete it you will have to delete all objects that reference it manually.
    # SQL equivalent: RESTRICT.



