from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect, HttpResponse
from message_board.models import Message
from django.contrib.auth.models import User
from django.conf import settings
from django.db import models
import datetime
import users.models
import main.models
from users.models import CustomUser
# Create your views here.

# Redirect user to login page if not logged in
@login_required(login_url='/accounts/login/')

def messageBoard(request):

    messageBoardNames = []
    studentClubEntities = main.models.StudentClubRelation(user_id=CustomUser.username).objects.all()
    for entity in studentClubEntities:
        clubName = main.models.Club(club_id=entity.club_id).objects.first().club_name
        portfolioName = main.models.Portfolio(position_id=entity.position_id).objects.first().portfolio_name
        if clubName not in messageBoardNames:
            messageBoardNames.append(clubName)
        if portfolioName not in messageBoardNames:
            messageBoardNames.append(portfolioName)

    messages = Message.objects.all()

    if not (request.user.is_superuser or request.user.is_staff):
        # your logic here
        return redirect("mainMessageBoardView")  # or your url name
    return render(request, 'message_board/Admin_message_board.html', {'messages': messages, 'messageboards': messageBoardNames})


def Messages(request):
    return render(request, 'Messages/messages.html')


def MainMessages(request):
    # return render(request, 'message_board/Main_Message_Board.html')
    messages = Message.objects.all()
    return render(request, 'Messages/messages.html', {'messages': messages})

# def messageBoard(request):
#     messages = Message.objects.all()
#     return render(request, 'message_board/Admin_message_board.html', {messages: messages})
#
# def Messages(request):
#     messages = Message.objects.all()
#     return render(request, 'Messages/messages.html', {messages : messages})

def ManageUsers(request):
    return render(request, 'message_board/Create_Users.html')

def ManageClubs(request):
    return render(request, 'message_board/Customise_Clubs.html')

def CustomiseUsers(request):
    return render(request, 'message_board/Customise_Users.html')

def SendMessage(request):
    if request.method == 'POST':
        if request.POST.get('header') and request.POST.get('body'):
            message = Message()
            message.message_header = request.POST.get('header')
            message.message_body = request.POST.get('body')
            message.user = users.models.CustomUser.objects.first()
            message.date_time = datetime.datetime.now()
            message.save()

    return render(request, 'message_board/Send_Message.html')


def MessageBoard(request):

    return render(request, 'message_board/Main_Message_Board.html')


def CustomiseClubs(request):
    return render(request, 'message_board/Customise_Clubs.html')


def MainMessages(request):
    return render(request, 'message_board/Main_Message_Board.html')

def UserProfile(request):
    return render(request, 'message_board/User_Profile.html')

def WSCHeader(request):
    return render(request, 'WSCHeader.html')

def ChairPerson(request):
    return render(request, 'message_board/Chair-Person-Messages.html')

def Treasurer(request):
    return render(request, 'message_board/Treasurer-Messages.html')
