from django.template import loader
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from post.forms import NewPostform
from django.http import HttpResponse
from post.models import Post, Stream

@login_required
def index(request):
    user = request.user
    posts = Stream.objects.filter(user=user)
    
    group_ids = []
    
    for post in posts:
        group_ids.append(post.post_id)
        
    post_items = Post.objects.filter(id__in=group_ids).all().order_by('-posted')
    
    context = {
        'post_items': post_items,
    }
    
    return render(request, 'home.html', context)