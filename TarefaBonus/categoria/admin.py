from django.contrib import admin

# Register your models here.

from django.contrib import admin

from .models import Categoria, Produto

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ("nomeProduto", "valor", "descricao", "categoria")

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_filter = ("categoria",)