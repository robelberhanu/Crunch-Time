from django.contrib import admin

# Register your models here.
from .models import Club, Portfolio, StudentClubRelation

admin.site.register(Portfolio)
# admin.site.register(StudentClubRelation)


class ClubAdmin(admin.ModelAdmin):
    list_display = ['club_id', 'club_name', 'is_deleted']


class StudentClubRelationAdmin(admin.ModelAdmin):
    list_display = ['id', 'club_id', 'user_id', 'portfolio_id', 'is_deleted']


admin.site.register(StudentClubRelation,StudentClubRelationAdmin)
admin.site.register(Club,ClubAdmin)

# class CustomUserAdmin(UserAdmin):
#     add_form = CustomUserCreationForm
#     form = CustomUserChangeForm
#     model = CustomUser
#     list_display = ['email', 'username','contact_number','is_active']