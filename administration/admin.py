from django.contrib import admin

# Register your models here.
from administration.models import Club
from administration.models import Position
from administration.models import Membership

admin.site.register(Club)
admin.site.register(Position)
admin.site.register(Membership)
