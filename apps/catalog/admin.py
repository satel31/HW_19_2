from django.contrib import admin
from apps.catalog.models import Category, Product, Contacts

# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('pk', 'category_name')

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('pk', 'product_name', 'unit_price', 'category',)
    list_filter = ('category',)
    search_fields = ('product_name', 'description',)

@admin.register(Contacts)
class ContactsAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'phone', 'email',)