from django.shortcuts import render
from .forms import PostForm
from .models import Post

def index(request):
    posts = Post.objects.all()
    return render(request, 'app/index.html', {'posts': posts})