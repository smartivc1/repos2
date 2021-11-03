from django.contrib import admin
from .models import Producto


@admin.register(Producto)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["nombreProducto", "user"]
    list_display_links = ["nombreProducto", "user"]
    search_fields = ["nombreProducto", "user"]

