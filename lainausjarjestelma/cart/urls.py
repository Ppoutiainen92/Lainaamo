from django.urls import path
from . import views

urlpatterns = [
    path("", views.cart, name="cart"),
    path("loaned_books", views.loaned_books, name="loaned_books")

]
