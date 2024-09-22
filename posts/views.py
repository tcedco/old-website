from django.shortcuts import render
from .models import Post

# Create your views here.

def home(request):
    return render(request, 'posts/index.html')

def posts(request):
    posts = Post.objects.all().order_by('-date_posted')
    return render(request, 'posts/posts.html', {'posts': posts})

def about(request):
    return render(request, 'posts/about.html', {'title': 'About'})