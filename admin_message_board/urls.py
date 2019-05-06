from django.urls import path

import main_message_board
import message_board
from . import views

urlpatterns = [
    path('', views.messageBoard, name='messageBoardView'),
    path('messages.messages.html', views.Messages, name='Messages'),
    path('message_board.Main_Message_Board.html', views.MainMessages, name='MainMessageBoard'),
    path('message_board.Manage_Users.html', views.ManageUsers, name='ManageUsers'),
    path('message_board.Manage_Clubs.html', views.ManageClubs, name='ManageClubs'),
    path('message_board.Customise_Users.html', views.CustomiseUsers, name='CustomiseUsers'),
    path('message_board.Send_Message.html', views.SendMessage, name='SendMessage'),
    path('message_board.Customise_Clubs.html', views.CustomiseClubs, name='CustomiseClub')

    # arguments for path function -
    # route (required)
    # view (required)
    # kwargs - Arbitrary keyword arguments can be passed in a dictionary to the target view
    # name - lets you refer to it unambiguously from elsewhere in Django
]

