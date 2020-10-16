from django.contrib import admin
from .models import OrderBook, Order

# Register your models here.
admin.site.register(OrderBook)
admin.site.register(Order)
