from django.shortcuts import render, get_object_or_404
from django.utils.html import mark_safe
from .models import Post

import markdown as md

# Create your views here.

def home(request):
    posts = Post.objects.order_by('-date_posted')[:3]
    return render(request, 'posts/index.html', {'posts': posts})

def posts(request):
    posts = Post.objects.all().order_by('-date_posted')
    return render(request, 'posts/posts.html', {'posts': posts})

def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    post.content = mark_safe(md.markdown(
        post.content,
        extensions=['fenced_code', 'codehilite']
    ))
    
    return render(request, 'posts/post_detail.html', {'post': post})

def about(request):
    return render(request, 'posts/about.html', {'title': 'About'})