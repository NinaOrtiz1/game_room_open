from django.contrib import admin

# Register your models here.
from .models import Catalogo, Producto

admin.site.register(Catalogo)
admin.site.register(Producto)
