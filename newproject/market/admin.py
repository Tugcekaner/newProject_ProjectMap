from django.contrib import admin
from .models import *

class CategoryView(admin.ModelAdmin):
    list_display = ['title','slug']

class ProductView(admin.ModelAdmin):
    list_display = ['title','category','stok','price']
    list_filter = ['category','price']

# Register your models here.
admin.site.register(Category,CategoryView)
admin.site.register(Product,ProductView)