from django.contrib import admin
from .models import Product

class ProductAdmin(admin.ModelAdmin):
    
    list_display = ['name', 'price', 'stock', 'available', 'created_at']
    
 
    list_display_links = ['name']
    
   
    list_filter = ['available', 'created_at']
    
    search_fields = ['name', 'description']
    
   
    list_editable = ['price', 'stock', 'available']

admin.site.register(Product, ProductAdmin)
