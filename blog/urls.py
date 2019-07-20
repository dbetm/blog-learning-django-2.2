from django.contrib import admin
from django.urls import path

# Importar las vistas de mi aplicación
from .views import(
    blog_post_detail_view,
    blog_post_list_view,
    blog_post_update_view,
    blog_post_delete_view,
)

# Se hace el mapeo de url's con vistas
urlpatterns = [
    # rutas de mi aplicación
    path('<str:slug>/', blog_post_detail_view),
    # con expresión regular
    # re_path(r'^blog/(?P<slug>\w+)/$', blog_post_detail_page),
    # Rutas del CRUD
    path('', blog_post_list_view),
    path('<str:slug>/edit', blog_post_update_view),
    path('<str:slug>/delete', blog_post_delete_view),
]
