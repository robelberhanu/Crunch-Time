from django.contrib import admin

# Register your models here.
from .models import Club, Portfolio, StudentClubRelation

admin.site.register(Club)
admin.site.register(Portfolio)
admin.site.register(StudentClubRelation)