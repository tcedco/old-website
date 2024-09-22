from django.shortcuts import render, get_object_or_404
from .models import Post

# Create your views here.

def home(request):
    return render(request, 'posts/index.html')

def posts(request):
    posts = Post.objects.all().order_by('-date_posted')
    return render(request, 'posts/posts.html', {'posts': posts})

def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, 'posts/post_detail.html', {'post': post})

def about(request):
    return render(request, 'posts/about.html', {'title': 'About'})