from django.shortcuts import render
from django.http import HttpResponse
from books.models import Book
from django.views import generic
from django.utils import timezone
from django.shortcuts import get_object_or_404
from libraries.models import LibraryBook
import logging
from django.shortcuts import redirect
from django.contrib import messages
from cart.models import Order, OrderBook
# Create your views here.


class BookListView(generic.ListView):
    model = Book
    context_object_name = 'books'
    template_name = 'books/book_list.html'
    paginate_by = 9

    # def showbooks(request):
    #     allbooks = Book.object.all()
    #     context = {'allbooks': allbooks}
    #     return render(request, 'books/book_list.html', context)


# class BookDetailView(generic.DetailView):
#     # model = Book
#     context_object_name = 'book'
#     template_name = 'books/detail.html'

#     def get_object(self):
#         id_ = self.kwargs.get("id")
#         return get_object_or_404(Book, id=id_)


def book_detail_view(request, pk):
    if request.method == "POST":
        """Add to cart logic in book_detail"""
        if request.user.is_authenticated:
            user = request.user
            user_order = Order.objects.filter(user__pk=user.id).first()
            # Getting right library_book from the query
            req_lib_book = request.POST.get("select")
            lib_book = LibraryBook.objects.filter(
                library__name=req_lib_book, book__pk=pk).first()
            if not OrderBook.objects.filter(library_book=lib_book).exists():
                # Creating new order_book object and add it to users order
                instance = OrderBook.objects.create(
                    library_book=lib_book, user=user)
                user_order.library_book.add(instance)
                logging.warning(lib_book.book.book_title)
                logging.warning(lib_book.library.name)
            else:
                logging.warning("Already exists")
            return redirect("book-list")
        else:
            messages.warning(
                request, f"Kirjaudu sisään ennen kuin lisäät kirjoja.")
            return redirect("login")
    else:
        book = Book.objects.filter(id=pk).first()
        library_books = LibraryBook.objects.filter(book__pk=pk)
        # Sums all available books
        total_amount = sum([lib.amount for lib in library_books])
        context = {"book": book, "library_books": library_books,
                   "total_amount": total_amount}
        return render(request, "books/book_detail.html", context)


# class BookDetailView(generic.DetailView):
    # model = Book
   #context_object_name = 'book_detail'
   #template_name = 'books/book_detail.html'

    # def book_detail_view(request, primary_key):
    #     try:
    #         book = Book.objects.get(pk=primary_key)
    #     except Book.DoesNotExist:
    #         raise Http404('Book does not exist')
    # else:
    #     return render(request, 'books/detail.html', context={'book': book})
