from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Order, OrderBook
from cart.models import LoanedBook
from libraries.models import LibraryBook
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
                change_library_book_amount(-1, book.library_book.id)
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
    # Returns book to library and update it's availability
    if request.method == "POST":
        selected_book_id = request.POST.get("delete")
        book = loaned_books.library_book.filter(id=selected_book_id).first()

        # Update librarybook amounts
        # Find right book from LibraryBook table
        # lib_book = LibraryBook.objects.filter(id=book.library_book.id).first()
        if book.library_book:
            change_library_book_amount(1, book.library_book.id)
        book.save()
        book.delete()
        return redirect("loaned_books")

    else:
        # GET request for loaned books
        tz = timezone.now()
        time_now = datetime.date(tz.year, tz.month, tz.day)
        # If book is expired change it's bool state
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


def change_library_book_amount(amount, book_id):
    lib_book = LibraryBook.objects.filter(id=book_id).first()
    lib_book.amount += amount
    lib_book.save()
