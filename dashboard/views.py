from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import UserRegisterForm
from .models import DataUser

def home(request):
    userData = DataUser.objects.all()
    return render(request, 'home.html', {'userData': userData})

def logout_user(request):
    logout(request)
    messages.success(request, "You Have Been Logged Out....")
    return redirect('home')

def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            # Profile.get_or_create(user=request.user)
            username = form.cleaned_data.get('username')
            messages.success(request, f'Hurray your account was created!!')

            # Automatically Log In The User
            new_user = authenticate(username=form.cleaned_data['username'],
                                    password=form.cleaned_data['password1'],)
            login(request, new_user)
            return redirect('home')
    elif request.user.is_authenticated:
        return redirect('home')
    else:
        form = UserRegisterForm()
    return render(request, 'login.html', {'form': form})
    