from django.contrib import admin

from .models import Category, Product
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('title',)}
    
admin.site.register(Category, CategoryAdmin)
admin.site.register(Product)