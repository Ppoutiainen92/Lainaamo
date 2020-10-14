from django.shortcuts import render
from django.http import HttpResponse
from books.models import Book
from django.views import generic
from django.utils import timezone
from django.shortcuts import get_object_or_404
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


class BookDetailView(generic.DetailView):
    model = Book
   #context_object_name = 'book_detail'
   #template_name = 'books/book_detail.html'

    def book_detail_view(request, primary_key):
        try:
            book = Book.objects.get(pk=primary_key)
        except Book.DoesNotExist:
            raise Http404('Book does not exist')
        # else:
        #     return render(request, 'books/detail.html', context={'book': book})
