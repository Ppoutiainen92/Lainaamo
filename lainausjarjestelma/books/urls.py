from django.urls import path
from . import views
from books.views import BookListView
from books import views as book_views

urlpatterns = [
    path('', BookListView.as_view(), name='book-list'),
    path('<int:pk>', book_views.book_detail_view, name='book-detail'),
    path('search/', book_views.search, name="search")
]
