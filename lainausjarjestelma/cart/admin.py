from django.contrib import admin
from .models import OrderBook, Order, LoanedBook


@admin.register(OrderBook)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("__str__", "is_expired")


# Register your models here.

admin.site.register(Order)
admin.site.register(LoanedBook)
