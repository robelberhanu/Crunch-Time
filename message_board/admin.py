from django.contrib import admin

# Register your models here.
from message_board.models import Message

admin.site.register(Message)
