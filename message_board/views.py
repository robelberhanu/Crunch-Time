from django.shortcuts import render

# Create your views here.


def messageBoard(request):
    return render(request, 'message_board/message_board.html')

