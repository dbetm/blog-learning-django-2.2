from django.db import models
"""
Los modelos permiten guardar los datos en la BD
"""

# Create your models here.

# Se declaran los campos que se mapean dentro de la BD
class BlogPost(models.Model):
    # id = models.IntegerField()  # se genera por defecto
    title = models.TextField()
    slug = models.SlugField(unique=True) # hello world -> hello-wordl
    content = models.TextField(null=True, blank=True)
