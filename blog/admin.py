from django.contrib import admin

from .models import Author, Category, Post


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ("nombre", "email")
    search_fields = ("nombre", "email")


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("nombre",)
    search_fields = ("nombre",)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("titulo", "autor", "categoria", "fecha_publicacion")
    list_filter = ("categoria", "autor")
    search_fields = ("titulo", "contenido")
