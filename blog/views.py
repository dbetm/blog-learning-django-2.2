from django.shortcuts import render, get_object_or_404
from django.http import Http404
# Create your views here.
from .models import BlogPost

# GET -> 1 object
# filter -> [] objects

# Modelo es una vista
def blog_post_detail_view(request, slug):
    # PRIMER FORMA
    # try:
    #     obj = BlogPost.objects.get(slug=slug)
    # except BlogPost.DoesNotExist:
    #     raise Http404
    # except ValueError:
    #     raise Http404
    # SEGUNDA FORMA
    # obt = get_object_or_404(BlogPost, slug=slug)

    # Cuando son varios objetos los que puede retornar
    # queryset = BlogPost.objects.filter(slug=slug)
    # if(queryset.count() == 0):
    #    raise Http404
    #obj = queryset.first()

    #forma completa considerando 404
    obj = get_object_or_404(BlogPost, slug=slug)
    template_name = 'blog/detail.html'
    context = {"object": obj}
    return render(request, template_name, context)

# CRUD (Create Retrieve Update Delete)
# GET Retrieve / List
# POST Create / Update / Delete

def blog_post_list_view(request):
    # listar los items, o de una búsqueda
    qs = BlogPost.objects.all() # queryset -> list of python objects
    # Filtros
    # qs = BlogPost.objects.filter(title__icontains="hello")
    template_name = "blog/list.html"
    # la convención es llamarle object_list
    context = {"object_list": qs}
    return render(request, template_name, context)

# retrieve
def blog_post_detail_view(request, slug):
    # Recuperar los datos de un objeto
    obj = get_object_or_404(BlogPost, slug=slug)
    template_name = 'blog/detail.html'
    context = {"object": obj}
    return render(request, template_name, context)

def blog_post_create_view(request):
    # Crear un objeto
    # uso de un form
    template_name = "blog/create.html"
    context = {"form": None}
    return render(request, template_name, context)

def blog_post_delete_view(request, slug):
    obj = get_object_or_404(BlogPost, slug=slug)
    template_name = 'blog/delete.html'
    context = {"object": obj}
    return render(request, template_name, context)

def blog_post_update_view(request, slug):
    obj = get_object_or_404(BlogPost, slug=slug)
    template_name = 'blog/update.html'
    context = {"object": obj, "form": None}
    return render(request, template_name, context)
