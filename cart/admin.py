from django.contrib import admin
from .models import *

class CartItemInline(admin.TabularInline):
    model = CartItem
    list_display = ['cart', 'variant', 'size', 'color', 'price', 'quantity', 'total_price']


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ['user', 'create_at', 'get_total_price']
    inlines = [CartItemInline]


@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ['cart', 'variant', 'size', 'color', 'price', 'quantity', 'total_price']

