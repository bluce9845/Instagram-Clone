from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from post.models import Post, Stream, Tag, Follow, Likes


@login_required
def UserProfile(request):
    user = request.user
    postValue = user.posts.count()
    posts = user.posts.all().order_by('-posted')
    post_items = Post.objects.filter(user=user).order_by('-posted')
    
    context = {
        'postValue': postValue,
        'user_posts': posts,
        # 'picture_user': picture_user,
        'user':user
    }
    
    print(f"This user posts : {post_items}")
    
    return render(request, 'profile.html', context)


@login_required
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

@login_required
def likeProfile(request, post_id):
    user = request.user
    post = Post.objects.get(id=post_id)
    current_likes = post.likes
    
    liked = Likes.objects.filter(user=user, post=post).count()
    
    if not liked:
        likes = Likes.objects.create(user=user, post=post)
        current_likes = current_likes + 1
    else:
        Likes.objects.filter(user=user, post=post).delete()
        current_likes = current_likes - 1
    
    post.likes = current_likes
    post.save()
    
    return redirect('profile')

@login_required
def likeOtherProfile(request, post_id):
    user = request.user
    post = Post.objects.get(id=post_id)
    current_likes = post.likes
    
    liked = Likes.objects.filter(user=user, post=post).count()
    
    if not liked:
        likes = Likes.objects.create(user=user, post=post)
        current_likes = current_likes + 1
    else:
        Likes.objects.filter(user=user, post=post).delete()
        current_likes = current_likes - 1
    
    post.likes = current_likes
    post.save()
    
    return redirect('profile')