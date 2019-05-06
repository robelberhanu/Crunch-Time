from django.http import HttpResponse
from django.template import loader

from users.forms import CustomUserCreationForm

from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from users.models import CustomUser


def register(request):
    # get users
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            # raw_password = form.cleaned_data.get('password1')
            raw_password = 'temp_password'  # Definitely do not keep this code!
            user = authenticate(username=username, password=raw_password)  # creates user
    else:
        form = UserCreationForm()
    return render(request, 'administration/create_user.html', {'form': form, 'user': CustomUser})


# def manage_users(request):
#     return HttpResponse("You're looking at the manage users page")

def manage_users(request):
    # User creation
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save(commit=False)
            username = form.cleaned_data.get('username')
            raw_password = 'temp'  # Will be changed below
            # Dunno if this is valid

            curr_user = CustomUser.objects.create_user(username=username, password=raw_password, email=None)
            # curr_user = authenticate(username=username, password=raw_password)
            # basically says that the user has no password - used for custom authentication i.e. LDAP
            curr_user.set_unusable_password()
            curr_user.save()
    else:
        form = CustomUserCreationForm()

    # Display users
    user_list = CustomUser.objects.all().values_list('username', flat=True),
    # usernames = user_list.values_list('username', flat=True),
    # return HttpResponse(template.render(context, request))
    # , 'usernames': usernames}
    return render(request, 'administration/manage_users.html', {'user_list': user_list, 'form':form})


def user(request, user_id):
    return HttpResponse("You're looking at user %s." % user_id)


def manage_clubs(request):
    return HttpResponse("You're looking at the manage clubs page")


def club(request, club_id):
    return HttpResponse("You're looking at club %s." % club_id)

