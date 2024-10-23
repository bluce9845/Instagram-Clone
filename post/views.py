from django.template import loader
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone
from post.forms import NewPostform
from django.http import HttpResponse, HttpResponseRedirect
from post.models import Post, Stream, Tag, Likes


@login_required
def index(request):
    user = request.user
    posts = Stream.objects.filter(user=request.user)

    print(f"User: {user} - ID: {user.id}")
    print(f"Posts for User {user}: {posts}")
    
    group_ids = []
    
    for post in posts:
        print(f"Post ID: {post.post_id}") 
        group_ids.append(post.post_id)
        
    post_items = Post.objects.filter(id__in=group_ids).all().order_by('-posted')
    
    print(post_items)

    # post_items = Stream.objects.all()
    
    template = loader.get_template('dashboard/test.html')
    
    context = {
        'post_items': post_items
    }
    
    return HttpResponse(template.render(context, request))

@login_required
def NewPost(request):
    user = request.user.id
    tags_objs = []
    
    if request.method == 'POST':
        form = NewPostform(request.POST, request.FILES)
        if form.is_valid():
            picture = form.cleaned_data.get('picture')
            caption = form.cleaned_data.get('caption')
            tags_form = form.cleaned_data.get('tags')
            
            tags_list = list(tags_form.split(','))
            
            for tag in tags_list:
                t, created = Tag.objects.get_or_create(title=tag.strip())
                tags_objs.append(t)
                
            p, created = Post.objects.get_or_create(picture=picture, caption=caption, user=request.user)
            # p, created = Post.objects.create(picture=picture, caption=caption, user=request.user)
            
            # duplikasi handling 
            stream, created = Stream.objects.get_or_create(post=p, user=request.user, defaults={'date': timezone.now()})

            
            p.tags.set(tags_objs)
            p.save()
            return redirect('home')
    else:
        form = NewPostform()
    
    context = {
        'form': form,
    }
    
    return render(request, 'newPost.html', context)


@login_required
def tags(request, tag_slug):
    tag = get_object_or_404(Tag, slug=tag_slug)
    posts = Post.objects.filter(tags=tag).order_by("-posted")
    
    context = {
        'posts': posts,
        'tag': tag,
    }
    
    return render(request, 'tag.html', context)

@login_required
def like(request, post_id):
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
    
    return redirect('home')