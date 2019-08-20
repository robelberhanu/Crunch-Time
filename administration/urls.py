from django.conf.urls import url
from django.urls import path

from . import views

urlpatterns = [
    # ex: /administration/users
    path('users/', views.manage_users, name='manage_users'),
    # ex: /administration/users/create
    path('users/create/', views.create_user, name='create_user'),
    # ex: /administration/user/1391994/
    path('users/<str:user_id>/', views.UserUpdateView.as_view(), name='user'),
    # ex: /administration/clubs
    path('clubs/', views.manage_clubs, name='manage_clubs'),
    # ex: /administration/clubs/create
    path('clubs/create/', views.create_club, name='create_club'),
    # ex: /administration/club/Throwy_Disk/
    path('clubs/<str:club_id>/', views.club, name='club'),
]
