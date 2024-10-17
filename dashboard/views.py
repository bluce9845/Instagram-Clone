from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import UserRegisterForm
from .models import DataUser
from django.template import loader
from post.models import Post,Tag, Stream, Follow 
from post.models import Post, Stream

def home(request):
    all_users = User.objects.all()
    userData = DataUser.objects.all()
    user = request.user
    posts = Stream.objects.filter(user=request.user)
    
    # Testing User
    print(f"User: {user} - ID: {user.id}")
    print(f"Posts for User {user}: {posts}")
    
    group_ids = []
    
    for post in posts:
        print(f"Post ID: {post.post.id}") 
        group_ids.append(post.post_id)
        
    post_items = Post.objects.filter(id__in=group_ids).all().order_by('-posted')
    
    # Post Debug
    print(post_items)
    
    context = {
        'all_users': all_users,
        'userData': userData,
        'post_items': post_items
    }
    return render(request, 'dashboard/home.html', context)

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
    return render(request, 'register.html', {'form': form})

def logout_user(request):
    logout(request)
    return redirect('login')


#================= TESTING ================#

def test(request):

    # post_items = Stream.objects.all()
    
    # template = loader.get_template('dashboard/test.html')
    
    # context = {
    #     'post_items': post_items
    # }
    
    return render(request, 'dashboard/test.html', {})

def PostTest(request):
    user = request.user
    
    post_items = Stream.objects.all().filter(user=user)
    if request.method == 'POST':
        picture = Post.objects.get['picture']
        caption = Post.objects.get['caption']
        tags_forms = Post.objects.get['tags']
        
        form = Stream.objects.get_or_create(picture=picture, caption=caption, tags=tags_forms, user=user)
        
        group_ids = []
        
        for group_id in group_ids:
            group_id.append()
            print(int(group_id))