from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from .models import Library
# Create your views here.


class LibraryListView(generic.ListView):
    model = Library
    context_object_name = "libraries"
    template_name = "libraries/library_list.html"
    paginate_by = 9


# class LibraryDetailView(generic.DetailView):
#     model = Library

#     def library_detail_view(request, primary_key):
#         try:
#             library = Library.objects.get(pk=primary_key)
#         except Library.DoesNotExist:
#             raise Http404("Library does not exist")
#         else:
#             return render(request, )
