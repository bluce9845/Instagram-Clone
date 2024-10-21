from django.shortcuts import get_object_or_404, render
from django.contrib.auth.models import User
from post.models import Post, Stream, Tag, Follow


def UserProfile(request):
    user = request.user
    postValue = user.posts.count()
    posts = user.posts.all()
        
    context = {
        'postValue': postValue,
        'user_posts': posts,
        'user': user,
    }
    
    return render(request, 'profile.html', context)


def OtherUserProfile(request, username):
    user = get_object_or_404(User, username=username)
    posts = Post.objects.filter(user=user)
    postValue = Post.objects.filter(user=user).count()

    context = {
        'profile_user': user,
        'posts': posts,
        'postValue': postValue,
    }
    
    return render(request, 'profile2.html', context)