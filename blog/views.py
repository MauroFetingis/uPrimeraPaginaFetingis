from django.shortcuts import redirect, render

from .forms import AuthorForm, CategoryForm, PostForm, PostSearchForm
from .models import Post


def index(request):
    ultimos_posts = Post.objects.select_related("autor", "categoria").order_by("-fecha_publicacion")[:5]
    return render(
        request,
        "blog/index.html",
        {
            "ultimos_posts": ultimos_posts,
        },
    )


def crear_autor(request):
    if request.method == "POST":
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("blog:index")
    else:
        form = AuthorForm()
    return render(request, "blog/crear_autor.html", {"form": form})


def crear_categoria(request):
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("blog:index")
    else:
        form = CategoryForm()
    return render(request, "blog/crear_categoria.html", {"form": form})


def crear_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("blog:index")
    else:
        form = PostForm()
    return render(request, "blog/crear_post.html", {"form": form})


def buscar_posts(request):
    resultados = None
    form = PostSearchForm(request.GET or None)
    if form.is_valid():
        termino = form.cleaned_data["termino"]
        resultados = Post.objects.filter(titulo__icontains=termino).select_related("autor", "categoria")
    return render(
        request,
        "blog/buscar_posts.html",
        {
            "form": form,
            "resultados": resultados,
        },
    )
