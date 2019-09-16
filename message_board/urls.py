from django.urls import path

from . import views

urlpatterns = [
    # First argument is the URL path NOT the name of the template...
    path('', views.messageBoard, name='messageBoardView'),
    path('messages.html', views.Messages, name='Messages'),
    # path('Create_Users.html', views.ManageUsers, name='ManageUsers'),
    # path('Manage_Clubs.html', views.ManageClubs, name='ManageClubs'),
    # path('Customise_Users.html', views.CustomiseUsers, name='CustomiseUsers'),
    path('Send_Message.html', views.SendMessage, name='SendMessage'),
    # path('Customise_Clubs.html', views.CustomiseClubs, name='CustomiseClub'),
    # path('Main_Message_Board.html', views.MainMessages, name='MainMessages'),
    # path('User_Profile.html', views.UserProfile, name='UserProfile'),
    # path('WSCHeader.html', views.WSCHeader, name='WSCHeader'),
    # path('Treasurer-Messages.html', views.Treasurer, name='Treasurer'),
    # path('Chair-Person-Messages.html', views.ChairPerson, name='Chair-Person'),

    # arguments for path function -
    # route (required)
    # view (required)
    # kwargs - Arbitrary keyword arguments can be passed in a dictionary to the target view
    # name - lets you refer to it unambiguously from elsewhere in Django
]

