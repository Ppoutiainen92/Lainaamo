from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Order, OrderBook
from cart.models import LoanedBook
import logging
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone
import datetime


@login_required
def cart(request):
    user = request.user
    if request.method == "POST":
        user = request.user
        if request.POST.get("buy"):
            # Loaning logic
            user_order = Order.objects.filter(user__pk=user.id).first()
            ordered_books = user_order.library_book.all()
            loaned_books = LoanedBook.objects.filter(user__pk=user.id).first()

            # Remove books from the cart and add them to loaned books
            for book in ordered_books:
                book.ordered = True
                book.expire_date = timezone.now() + timezone.timedelta(days=30)
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
        # Send ordered books to cart page
        order = Order.objects.filter(user=user, is_ordered=False).first()
        if order is not None:
            order_books = order.library_book.all()
            context = {"order_books": order_books, "order": order}
            return render(request, "cart/cart.html", context)
        else:
            return render(request, "cart/cart.html")


@login_required
def loaned_books(request):
    user = request.user
    loaned_books = LoanedBook.objects.filter(user=user).first()
    books = loaned_books.library_book.all()
    tz = timezone.now()
    time_now = datetime.date(tz.year, tz.month, tz.day)
    for book in books:
        exp = book.expire_date
        if book.expire_date > time_now:
            logging.warning("aikaa jäljellä")
            book.is_expired = False
            book.save()

        else:
            logging.warning("myöhässä")
            book.is_expired = True
            book.save()

    context = {"loaned_books": loaned_books, "books": books}
    return render(request, "cart/loaned_books.html", context)
