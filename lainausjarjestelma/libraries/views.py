from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from .models import Library, LibraryBook
from django.shortcuts import get_object_or_404
# Create your views here.


class LibraryListView(generic.ListView):
    model = Library
    context_object_name = "libraries"
    template_name = "libraries/library_list.html"
    paginate_by = 9


# def library_detail_view(request, primary_key):
#     try:
#         library = Library.objects.get(pk=mar)
#     except Library.DoesNotExist:
#         raise Http404("Library does not exist")
#     else:
#         return render(request, "libraries/library_detail.html", context={"library": library})

def library_detail_view(request, pk):
    library = Library.objects.filter(id=pk)
    library_books = LibraryBook.objects.filter(library__pk=pk)
    context = {"library": library, "library_books": library_books}
    return render(request, "libraries/library_detail.html", context)
