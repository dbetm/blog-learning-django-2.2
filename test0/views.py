# La arquitectura de Django es:
# Model:
# View: Define que acciones se pueden hacer, donde se define que se responde
#       cuando cuando se pide algún recurso.
# Template:

from django.http import HttpResponse
from django.shortcuts import render
# Para cargar cualquier tipo de template
from django.template.loader import get_template

#Don't Repeat Yourself (DRY)

def home_page(request):
    # Rendered with context
    my_title = "Hello there..."
    context = {"title": my_title}
    if request.user.is_authenticated:
        context.update({"my_list": [1, 2, 3, 4]})
    return render(request, "home.html", context)

def about_page(request):
    # Render con contexto
    return render(request, "about.html", {"title": "About us"})

def contact_page(request):
    return HttpResponse("<h1>Contact</h1>")

def example_page(request):
    context = {"title": "Example"}
    template_name = "hello_world.html"
    template_obj = get_template(template_name)
    rendered_item = template_obj.render(context)
    return HttpResponse(rendered_item)
