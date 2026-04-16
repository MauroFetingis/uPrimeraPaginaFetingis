from django.urls import path

from . import views

app_name = "blog"

urlpatterns = [
    path("", views.index, name="index"),
    path("autor/nuevo/", views.crear_autor, name="crear_autor"),
    path("categoria/nueva/", views.crear_categoria, name="crear_categoria"),
    path("post/nuevo/", views.crear_post, name="crear_post"),
    path("buscar/", views.buscar_posts, name="buscar_posts"),
]

