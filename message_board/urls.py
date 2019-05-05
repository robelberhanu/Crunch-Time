from django.urls import path

from . import views

urlpatterns = [
    path('', views.messageBoard, name='messageBoardView'),
    path('messages.html', views.Messages, name='Messages'),
    path('Main_Message_Board.html', views.MainMessages, name='MainMessageBoard'),
    path('Manage_Users.html', views.ManageUsers, name='ManageUsers'),
    path('Manage_Clubs.html', views.ManageClubs, name='ManageClubs'),
    path('Customise_Users.html', views.CustomiseUsers, name='CustomiseUsers'),
    path('Send_Message.html', views.SendMessage, name='SendMessage'),
    path('Customise_Clubs.html', views.CustomiseClubs, name='CustomiseClub')

    # arguments for path function -
    # route (required)
    # view (required)
    # kwargs - Arbitrary keyword arguments can be passed in a dictionary to the target view
    # name - lets you refer to it unambiguously from elsewhere in Django
]

