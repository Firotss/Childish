from django.contrib import admin
from .models import Product, Order

@admin.register(Product)
class RequestDemoAdmin(admin.ModelAdmin):
  list_display = [field.name for field in
Product._meta.get_fields()]

# @admin.register(Order)
# class RequestDemoAdmin(admin.ModelAdmin):
#   list_display = [field.name for field in
# Order._meta.get_fields()]