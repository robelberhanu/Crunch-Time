from django.urls import path

from . import views

urlpatterns = [
    path('', views.messageBoard, name='messageBoardView'),
    path('messages.html', views.Messages),
    # path('Main_Message_Board.html', views.MainMessages),
    # path('Create_Users.html', views.ManageUsers),
    # path('Manage_Clubs.html', views.ManageClubs)
    # arguments for path function -
    # route (required)
    # view (required)
    # kwargs - Arbitrary keyword arguments can be passed in a dictionary to the target view
    # name - lets you refer to it unambiguously from elsewhere in Django
]

