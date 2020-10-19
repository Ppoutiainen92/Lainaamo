from django.contrib import admin
from .models import OrderBook, Order, LoanedBook


# @admin.register(Order)
# class OrderAdmin(admin.ModelAdmin):
#     list_display = ("__str__", "is_ordered")

# Register your models here.
admin.site.register(OrderBook)
admin.site.register(Order)
admin.site.register(LoanedBook)
