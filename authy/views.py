from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse, resolve
from django.db import transaction
from post.models import Post, Stream, Tag, Follow, Likes
from .models import Profile
from post.models import Post


@login_required
def UserProfile(request, username):
    user = request.user
    postValue = user.posts.count()
    post_items = Post.objects.filter(user=user).order_by('-posted')
    profile = Profile.objects.get(user=user)
    url_name = resolve(request.path).url_name
    follower_count = Follow.objects.filter(follower=user).count()
    following_count = Follow.objects.filter(following=user).count()
    
    if url_name == 'profile':
        posts = Post.objects.filter(user=user).order_by("-posted")
    else:
        posts = profile.favorites.all()
        
    # url name test get url from browser
    print(f"Url name from name urls : {url_name}")
    
    context = {
        'postValue': postValue,
        'user_posts': posts,
        'url_name': url_name,
        'user': user,
        'follower_count': follower_count,
        'following_count': following_count,
    }
    
    print(f"This user posts : {post_items}")
    
    return render(request, 'profile.html', context)


@login_required
def OtherUserProfile(request, username):
    user = get_object_or_404(User, username=username)
    posts = Post.objects.filter(user=user).order_by("-posted")
    postValue = Post.objects.filter(user=user).count()
    profile = Post.objects.filter(user=user).all()
    follower_count = Follow.objects.filter(following=user).count()
    following_count = Follow.objects.filter(follower=user).count()
    
    # Check follow status
    follow_status = Follow.objects.filter(following=user, follower=request.user).exists()

    # Debug
    print(f"This user in profile variable : {profile}")

    context = {
        'user': user,
        'posts': posts,
        'postValue': postValue,
        'follow_status': follow_status,
        'profile': profile,
        'following_count': following_count,
        'follower_count': follower_count,
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

@login_required
def follow(request, username, option):
    user = request.user
    following = get_object_or_404(User, username=username)
    
    # Debug
    print(f"This following user for user {user} : {following}")
    
    try:
        f, cretaed = Follow.objects.get_or_create(follower=user, following=following)
        
        if int(option) == 0:
            f.delete()
            Stream.objects.filter(following=following, user=user).all().delete()
        else:
            posts = Post.objects.all().filter(user=following)[:10]
            
            with transaction.atomic():
                for post in posts:
                    stream = Stream(post=post, user=user, date=post.posted, following=following)
                    stream.save()

        return HttpResponseRedirect(reverse('authy:profile_other', args=[username]))
    except User.DoesNotExist:
        return HttpResponseRedirect(reverse('authy:profile_other', args=[username]))