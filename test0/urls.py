"""test0 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path, include # url
from .views import (
    home_page,
    about_page,
    contact_page,
    example_page
)
# Importar las vistas de mi aplicación
from blog.views import(
    blog_post_create_view,
)

# Se hace el mapeo de url's con vistas
urlpatterns = [
    path('', home_page),
    path('page/', about_page),
    # path('pages', about_page),
    # permite definir el nombre como una expresión regular
    re_path(r'^pages?/$', about_page),
    re_path(r'^about/$', about_page),
    # path('about/', about_page),
    path('contact/', contact_page),
    path('admin/', admin.site.urls),
    path('example/', example_page),
    # rutas de mi aplicación
    path('blog/', include('blog.urls')),
    path('blog-new/', blog_post_create_view),
]
