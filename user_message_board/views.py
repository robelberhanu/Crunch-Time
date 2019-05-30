from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from message_board.models import Message

# Create your views here.

# Redirect user to login page if not logged in
@login_required(login_url='/accounts/login/')

def MainMessages(request):
    messages = Message.objects.all()
    return render(request, 'message_board/Main_Message_Board.html', {'messages': messages})


def Messages(request):
    return render(request, 'Messages/messages.html')