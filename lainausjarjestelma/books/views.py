from django.shortcuts import render
from django.http import HttpResponse
from books.models import Book
from django.views import generic
from django.utils import timezone
# Create your views here.


class BookListView(generic.ListView):
    model = Book
    context_object_name = 'book_list'
    template_name = 'books/book_list.html'

    def showbooks(request):
        allbooks = Book.object.all()
        context = {'allbooks': allbooks}
        return render(request, 'books/book_list.html', context)
