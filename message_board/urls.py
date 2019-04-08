from django.urls import path

from . import views

urlpatterns = [
    path('', views.messageBoard, name='messageBoardView'),
    path('messages.html', views.Messages)
    # arguments for path function -
    # route (required)
    # view (required)
    # kwargs - Arbitrary keyword arguments can be passed in a dictionary to the target view
    # name - lets you refer to it unambiguously from elsewhere in Django
]

