from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Order, OrderBook
from cart.models import LoanedBook
import logging
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required


@login_required
def cart(request):
    user = request.user
    if request.method == "POST":
        if request.POST.get("buy"):
            # Loaning logic
            user = request.user
            user_order = Order.objects.filter(user__pk=user.id).first()
            ordered_books = user_order.library_book.all()
            loaned_books = LoanedBook.objects.filter(user__pk=user.id).first()

            # Remove books from the cart and add them to loaned books
            for book in ordered_books:
                book.ordered = True
                loaned_books.library_book.add(book)
                user_order.library_book.remove(book)
                book.save()

            return redirect("cart")
        else:
            # Deleting books from cart
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


@login_required
def loaned_books(request):
    return HttpResponse("Hello")
