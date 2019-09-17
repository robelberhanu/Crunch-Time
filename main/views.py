from django.shortcuts import render, redirect


# Create your views here.
def home(request):
    if request.user.is_staff:
        return redirect('messageBoardView')
    else:
        return redirect('mainMessageBoardView')

