from django.shortcuts import render

# Create your views here.


def messageBoard(request):
    return render(request, 'message_board/Admin_message_board.html')

def Messages(request):
    return render(request, 'Messages/messages.html')

def MainMessages(request):
    return render(request,'message_board/Main_Message_Board.html')

def ManageUsers(request):
    return render(request, 'message_board/Manage_Users.html')

def ManageClubs(request):
    return render(request, 'message_board/Manage_Clubs.html')

def CustomiseUsers(request):
    return render(request, 'message_board/Customise_Users.html')