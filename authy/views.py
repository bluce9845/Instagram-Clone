from django.shortcuts import get_object_or_404, render
from django.contrib.auth.models import User
from django.urls import reverse
from post.models import Post, Stream, Tag, Follow


def UserProfile(request):
    user = request.user
    postValue = user.posts.count()
    posts = user.posts.all().order_by('-posted')
    
    context = {
        'postValue': postValue,
        'user_posts': posts,
        # 'picture_user': picture_user,
        'user':user
    }
    
    return render(request, 'profile.html', context)


def OtherUserProfile(request, username):
    profile_user = get_object_or_404(User, username=username)
    posts = Post.objects.filter(user=profile_user).order_by("-posted")
    postValue = Post.objects.filter(user=profile_user).count()

    context = {
        'profile_user': profile_user,
        'posts': posts,
        'postValue': postValue,
    }
    
    return render(request, 'profile2.html', context)