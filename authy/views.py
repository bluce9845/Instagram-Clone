from django.shortcuts import get_object_or_404, render
from django.contrib.auth.models import User


def UserProfile(request, username):
    return render(request, 'profile.html', {})

def OtherUserProfile(request, username):
    user = get_object_or_404(User, username=username)
    context = {
        'user_profile': user,
    }
    return render(request, 'profile2.html', context)