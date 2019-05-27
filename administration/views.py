from django.contrib.admin.views.decorators import staff_member_required
from django.core.checks import messages
from django.http import HttpResponse
from django.template import loader

from users.forms import CustomUserCreationForm

from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, get_object_or_404
from users.models import CustomUser


from django.contrib.auth.decorators import login_required
# Redirect user to login page if not logged in
@login_required(login_url='/accounts/login/')


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


# instead of deleting a user to avoid issues with the database
def deactivate_user(request, username):
    obj = CustomUser.objects.get(pk=username)
    obj.is_active = False
    obj.save()
    return render(request, 'administration/manage_users.html')


def user(request, user_id):
    return HttpResponse("You're looking at user %s." % user_id)


def manage_clubs(request):
    return HttpResponse("You're looking at the manage clubs page")


def club(request, club_id):
    return HttpResponse("You're looking at club %s." % club_id)

