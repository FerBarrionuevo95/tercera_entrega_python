from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm

def index(request):
    posts = Post.objects.all()
    return render(request, 'app/index.html', {'posts': posts})


def crear_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            Post.objects.create(
                titulo=form.cleaned_data['titulo'],
                contenido=form.cleaned_data['contenido']
            )
            return redirect('index')
    else:
        form = PostForm()

    return render(request, 'app/crear.html', {'form': form})

def buscar(request):
    resultados = []

    if request.GET.get("titulo"):
        titulo = request.GET.get("titulo")
        resultados = Post.objects.filter(titulo__icontains=titulo)

    return render(request, 'app/buscar.html', {'resultados': resultados})