from django import forms

from .models import Author, Category, Post


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ["nombre", "email", "bio"]


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ["nombre", "descripcion"]


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["titulo", "contenido", "autor", "categoria"]


class PostSearchForm(forms.Form):
    termino = forms.CharField(
        label="Buscar por título",
        max_length=100,
        required=True,
    )

