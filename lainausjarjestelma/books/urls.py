from django.urls import path
from . import views
from books.views import BookListView

urlpatterns = [
    path('', BookListView.as_view(), name='book-list'),
]
