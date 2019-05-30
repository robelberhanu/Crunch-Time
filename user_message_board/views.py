from django.shortcuts import render, redirect
from message_board.models import Message

# Create your views here.

def MainMessages(request):
    messages = Message.objects.all()
    if (request.user.is_superuser or request.user.is_staff):
        # your logic here
        return redirect("messageBoardView")  # or your url name
    return render(request, 'message_board/Main_Message_Board.html', {'messages': messages})


def Messages(request):
    return render(request, 'Messages/messages.html')