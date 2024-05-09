from django.contrib import admin
from .models import *

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    list_display = ['order', 'variant', 'size', 'type', 'price', 'quantity', 'total_price']


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'customer_name', 'customer_phone_number', 'create_at', 'get_total_price']
    inlines = [OrderItemInline]


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['id', 'order', 'variant', 'size', 'type', 'price', 'quantity', 'total_price']

