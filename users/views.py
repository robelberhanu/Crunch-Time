from django.shortcuts import render

from django.shortcuts import render

from django.shortcuts import get_object_or_404
from .models import CustomUser


def user_profile_view(request):
    # custom_user = get_object_or_404(CustomUser, id=id)

    # context = {'customUser': custom_user,}

    return render(request, 'users/user_profile.html')

