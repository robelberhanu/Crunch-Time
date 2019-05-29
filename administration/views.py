from django.contrib.admin.views.decorators import staff_member_required
from django.core.checks import messages
from django.http import HttpResponse
from django.shortcuts import redirect
from django.template import loader
from django.contrib.auth.decorators import login_required

from users.forms import CustomUserCreationForm

from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, get_object_or_404
from users.models import CustomUser


# Redirect user to login page if not logged in
@login_required(login_url='/accounts/login/')


def manage_users(request):
    # Display users
    username_list = CustomUser.objects.all().values_list('username', flat=True),
    user_list = list(CustomUser.objects.all())
    # usernames = user_list.values_list('username', flat=True),
    # return HttpResponse(template.render(context, request))
    # , 'usernames': usernames}
    return render(request, 'administration/manage_users.html', {'username_list': username_list, 'user_list': user_list})


def create_user(request):
    # User creation
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save(commit=False)
            username = form.cleaned_data.get('username')
            first_name = form.data.get('first_name')
            last_name = form.data.get('last_name')
            email = form.data.get('email')
            contact_number = form.data.get('contact_number')
            id_number = form.data.get('id_number')
            dob = str(id_number)[:6]
            raw_password = dob  # Will be changed below

            # Dunno if this is valid
            curr_user = CustomUser.objects.create_user(username=username, password=raw_password, email=email, first_name=first_name, last_name=last_name, contact_number=contact_number, id_number=id_number)
            # curr_user = authenticate(username=username, password=raw_password)
            # basically says that the user has no password - used for custom authentication i.e. LDAP
            # curr_user.set_unusable_password()
            curr_user.save()
            # redirect back to manage_users
            return redirect(manage_users)
    else:
        form = CustomUserCreationForm()
    return render(request, 'administration/create_user.html', {'form': form})


# instead of deleting a user to avoid issues with the database - rather delete for the moment
def deactivate_user(request, username):
    obj = CustomUser.objects.get(pk=username)
    obj.is_active = False
    obj.save()
    return render(request, 'administration/manage_users.html')


def user(request, user_id):
    print(user_id)
    return HttpResponse("You're looking at user %s." % user_id)


def manage_clubs(request):
    return HttpResponse("You're looking at the manage clubs page")


def club(request, club_id):
    return HttpResponse("You're looking at club %s." % club_id)

