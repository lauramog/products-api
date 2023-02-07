from django.contrib import admin
from .models import Product

# Register your models here.

@admin.register(Product)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description')