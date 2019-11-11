from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from django.shortcuts import render

from django.shortcuts import get_object_or_404
from .models import CustomUser


# Redirect user to login page if not logged in
@login_required(login_url='/accounts/login/')

def user_profile_view(request):
    # custom_user = get_object_or_404(CustomUser, id=id)

    # context = {'customUser': custom_user,}

    return render(request, 'users/user_profile.html')

