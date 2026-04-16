from django.db import models


class Author(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    bio = models.TextField(blank=True)

    def __str__(self) -> str:
        return self.nombre


class Category(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField(blank=True)

    def __str__(self) -> str:
        return self.nombre


class Post(models.Model):
    titulo = models.CharField(max_length=200)
    contenido = models.TextField()
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    autor = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="posts")
    categoria = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, related_name="posts")

    def __str__(self) -> str:
        return self.titulo
