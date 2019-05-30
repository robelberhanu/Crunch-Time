from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect, HttpResponse
from message_board.models import Message
from django.contrib.auth.models import User
from django.conf import settings
from django.db import models
import datetime
import users.models
# Create your views here.

# Redirect user to login page if not logged in
@login_required(login_url='/accounts/login/')

def messageBoard(request):
    messages = Message.objects.all()
    return render(request, 'message_board/Admin_message_board.html', {'messages': messages})


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


def CustomiseClubs(request):
    return render(request, 'message_board/Customise_Clubs.html')
