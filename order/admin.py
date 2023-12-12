
from django.contrib import admin
from .models import Order, OrderItem

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 1

class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'order_date', 'total_price')
    list_display_links =('id', 'user')
    inlines = [OrderItemInline]

admin.site.register(Order, OrderAdmin)
