# Tercer Entrega - Blog en Django

Proyecto simple de blog desarrollado para la tercera entrega de CoderHouse.  
Implementa el patrón MVT de Django, herencia de plantillas, tres modelos y formularios para crear y buscar datos.

## Cómo ejecutar el proyecto

1. Crear y activar un entorno virtual de Python (opcional pero recomendado).
2. Instalar dependencias:

```bash
python -m pip install django
```

3. Aplicar migraciones:

```bash
python manage.py migrate
```

4. Crear un superusuario (para entrar al admin de Django):

```bash
python manage.py createsuperuser
```

5. Levantar el servidor de desarrollo:

```bash
python manage.py runserver
```

6. Abrir en el navegador:
- Sitio principal: `http://127.0.0.1:8000/`
- Admin de Django: `http://127.0.0.1:8000/admin/`

## Funcionalidades y orden sugerido de prueba

1. **Panel de administración**
   - Entrar a `http://127.0.0.1:8000/admin/` con el superusuario creado.
   - Verás los modelos `Authors`, `Categories` y `Posts` registrados.

2. **Página de inicio (`index`)**
   - URL: ruta raíz `/`.
   - Muestra los últimos 5 posts creados.
   - Plantilla `index.html` hereda de `base.html`.

3. **Crear autor**
   - Desde el menú superior, ir a **"Nuevo autor"**.
   - URL con nombre: `blog:crear_autor`.
   - Formulario basado en `AuthorForm` para crear registros del modelo `Author`.

4. **Crear categoría**
   - Desde el menú superior, ir a **"Nueva categoría"**.
   - URL con nombre: `blog:crear_categoria`.
   - Formulario basado en `CategoryForm` para crear registros del modelo `Category`.

5. **Crear post**
   - Desde el menú superior, ir a **"Nuevo post"**.
   - URL con nombre: `blog:crear_post`.
   - Formulario basado en `PostForm` para crear registros del modelo `Post`, relacionando autor y categoría.
   - Al guardar, redirige a la página de inicio.

6. **Buscar posts en la BD**
   - Desde el menú superior, ir a **"Buscar"**.
   - URL con nombre: `blog:buscar_posts`.
   - Formulario simple (`PostSearchForm`) que busca posts por título utilizando `icontains`.
   - Muestra la lista de resultados con título, autor y categoría.

## Estructura principal del proyecto

- **Proyecto Django**: `SpacingAway`
  - `settings.py`: se registra la app `blog` en `INSTALLED_APPS` y se configura el idioma en español (`es-ar`).
  - `urls.py`: incluye las URLs de la app `blog` con `path('', include('blog.urls'))`.

- **App Django**: `blog`
  - `models.py`:
    - `Author`: nombre, email, bio.
    - `Category`: nombre, descripción.
    - `Post`: título, contenido, fecha de publicación, autor (FK), categoría (FK).
  - `admin.py`: registro de los tres modelos en el admin con algunas columnas de ayuda.
  - `forms.py`: `AuthorForm`, `CategoryForm`, `PostForm` y `PostSearchForm`.
  - `views.py`: vistas para:
    - `index`
    - `crear_autor`
    - `crear_categoria`
    - `crear_post`
    - `buscar_posts`
  - `urls.py`: rutas con nombre para cada una de las vistas anteriores.
  - `templates/blog/`:
    - `base.html`: plantilla base con navegación y bloques `{% block title %}` y `{% block content %}`.
    - `index.html`: hereda de `base.html`, muestra últimos posts.
    - `crear_autor.html`: formulario para autores.
    - `crear_categoria.html`: formulario para categorías.
    - `crear_post.html`: formulario para posts.
    - `buscar_posts.html`: formulario y resultados de búsqueda.

Con esto se cumplen los requisitos de la consigna: proyecto Django con patrón MVT, herencia de plantillas, tres modelos, formularios para inserción de datos y un formulario para buscar en la base de datos, además de este `README` explicando cómo probar las funcionalidades.

