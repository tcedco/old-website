from django.shortcuts import render
from .models import Post

# Create your views here.

def post_list(request):
    posts = Post.objects.all().order_by('-date_posted')
    return render(request, 'posts/post_list.html', {'posts': posts})