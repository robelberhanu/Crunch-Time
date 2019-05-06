from django.shortcuts import render
from message_board.models import Message

# Create your views here.


def MainMessages(request):
    messages = Message.objects.all()
    return render(request, 'message_board/Main_Message_Board.html', {'messages':messages})


def Messages(request):
    return render(request, 'Messages/messages.html')
