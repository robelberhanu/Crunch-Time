from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from message_board.models import Message
from main.models import StudentClubRelation, Club, Portfolio
from django.urls import resolve

# Create your views here.

# Redirect user to login page if not logged in
@login_required(login_url='/accounts/login/')


def MainMessages(request):

    messageBoardNames = []
    curr_user = request.user
    studentClubEntities = StudentClubRelation.objects.filter(user_id=curr_user)
    # studentClubEntities = main.models.StudentClubRelation(user_id=curr_user).objects.all()
    for entity in studentClubEntities:
        # user = CustomUser.objects.get(pk=form.data.get('user_id'))
        clubName = Club.objects.get(club_id=entity.club_id.club_id).club_name
        # portfolioName = main.models.Portfolio(position_id=entity.position_id).objects.first().portfolio_name
        # No idea if following will work
        portfolioName = Portfolio.objects.filter(portfolio_id = entity.portfolio_id.portfolio_id).first().portfolio_name
        if clubName not in messageBoardNames:
            messageBoardNames.append(clubName)
        if portfolioName not in messageBoardNames:
            messageBoardNames.append(portfolioName)

    url = request.get_full_path(False)

    messageBoard = ''
    i = url.find('=')
    if i == -1:
        messageBoard = "main"
    else:
        messageBoard = url[i+1:]

    messages = Message.objects.filter(message_board_name=messageBoard)

    print(messages)

    return render(request, 'message_board/Main_Message_Board.html', {'messages': messages, 'messageboards': messageBoardNames, 'messageboard': messageBoard})


def Messages(request):
    return render(request, 'Messages/messages.html')