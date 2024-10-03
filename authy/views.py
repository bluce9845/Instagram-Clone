from django.shortcuts import render


def UserProfile(request, username):
    return render(request, 'profile.html', {})