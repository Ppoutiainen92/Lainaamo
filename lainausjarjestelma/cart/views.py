from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Order, OrderBook
import logging
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required


@login_required
def cart(request):
    user = request.user
    if request.method == "POST":
        if request.POST.get("buy"):
            logging.warning("Osta")
            return redirect("cart")
        else:
            selected_book_id = request.POST.get("delete")
            logging.warning(selected_book_id)
            OrderBook.objects.filter(id=selected_book_id).delete()
            return redirect("cart")
    else:
        order = Order.objects.filter(user=user, is_ordered=False).first()
        if order is not None:
            order_books = order.library_book.all()
            context = {"order_books": order_books, "order": order}
            return render(request, "cart/cart.html", context)
        else:
            return render(request, "cart/cart.html")
